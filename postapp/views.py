from itertools import chain
from operator import attrgetter
import os
from user.models import Users
from rest_framework.response import Response
from rest_framework import status
from pollapp.models import Poll, PollOption
from pollapp.serializers import PollSerializer, PollSerializer2
from .models import Post, Comment, Like, Notifications
from .serializers import PostSerializer, CommentSerializer, PostPollSerializer, PollOptionSerializer2, NotificationSerializer, PostPollSerializer2
import datetime
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from datetime import datetime
import requests
from bs4 import BeautifulSoup
from pdf2image import convert_from_path
import cloudinary
import subprocess
from rest_framework.pagination import LimitOffsetPagination
from django.db.models import Q
from .utils import *
from rest_framework import filters
import time


class MyPagination(LimitOffsetPagination):
    default_limit = 10
    max_limit = 100


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user_posts(request, pk):
    paginator = MyPagination()
    posts = paginator.paginate_queryset(
        Post.objects.filter(created_by=pk).order_by('-id'), request)
    for post in posts:
        if post.Liked_by.filter(id=request.user.id).exists():
            post.is_liked = True
        else:
            post.is_liked = False
    serializer = PostSerializer(posts, many=True)
    return paginator.get_paginated_response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_posts(request):
    paginator = MyPagination()
    posts = paginator.paginate_queryset(
        Post.objects.all().order_by('-id'), request)
    print(posts)
    for post in posts:
        if post.Liked_by.filter(id=request.user.id).exists():
            post.is_liked = True
        else:
            post.is_liked = False

    serializer = PostSerializer(posts, many=True)
    return paginator.get_paginated_response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_post(request, pk):
    post = Post.objects.get(id=pk)
    post.is_liked = request.user in post.Liked_by.all()
    serializer = PostSerializer(post, many=False)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_post(request):
    data = request.data
    post = Post.objects.create(
        title=data['title'],
        content=data['content'],
        created_by=request.user,
        post_image=data['post_image'],
        created_at=datetime.now(),  # type: ignore
        allow_comments=data['allow_comments']
    )
    serializer = PostSerializer(post, many=False)
    return Response(serializer.data)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_post(request, pk):
    post = Post.objects.get(id=pk)
    if request.user != post.created_by:
        return Response({'detail': 'Not authorized to update this post'}, status=status.HTTP_400_BAD_REQUEST)
    data = request.data
    post = Post.objects.get(id=pk)
    post.title = data['title']
    post.content = data['content']
    post.post_image = data['post_image']
    post.last_modified_by = request.user
    post.is_liked = request.user in post.Liked_by.all()
    post.last_modified_at = datetime.now()  # type: ignore
    post.allow_comments = data['allow_comments']
    post.save()
    serializer = PostSerializer(post, many=False)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def delete_post(request, pk):
    post = Post.objects.get(id=pk)
    if request.user != post.created_by:
        return Response({'detail': 'Not authorized to delete this post'}, status=status.HTTP_400_BAD_REQUEST)
    post.delete()
    return Response({'detail': 'Post deleted'}, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getUserDetails(request):
    data = request.data
    user_name = data['username']
    user = Users.objects.get(username=user_name)
    return Response({'user': user.id,
                     'username': user.username,
                     'user_post_count': Post.objects.filter(created_by=user).count(),
                     'user_poll_count': Poll.objects.filter(created_by=user).count(),
                     'first_name': user.first_name,
                     'last_name': user.last_name,
                     'user_image': user.image,
                     })


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_posts_count(request):
    posts = Post.objects.all()
    count = posts.count()
    return Response({'count': count})


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_comment(request):
    data = request.data
    post_id = data.get('post_id')
    poll_id = data.get('poll_id')
    comment_id = data.get('comment_id')
    if post_id or poll_id or comment_id:
        if post_id:
            post = Post.objects.get(id=post_id)
            post_owner = post.created_by
            post_owner_fcm_token = post_owner.fcm_token  # type: ignore
            comment = Comment.objects.create(
                post=post,
                created_by=request.user,
                content=request.data['content'],
                created_at=datetime.now()  # type: ignore
            )
            post.comment_count += 1
            post.save()
            serializer = CommentSerializer(comment, many=False)
            if post_owner == comment.created_by:
                return Response(serializer.data)
            else:
                notification = Notifications.objects.create(
                    type='comment',
                    created_at=datetime.now(),  # type: ignore
                    created_by=request.user,
                    created_for=post_owner,
                    post=post,
                    content=request.data['content']

                )
                notification.save()
                send_noti_comments_post(post, comment, post_owner_fcm_token)
                return Response(serializer.data)
        elif poll_id:
            poll = Poll.objects.get(id=poll_id)
            poll_owner = poll.created_by
            poll_owner_fcm_token = poll_owner.fcm_token  # type: ignore
            comment = Comment.objects.create(
                poll=poll,
                created_by=request.user,
                content=request.data['content'],
                created_at=datetime.now()  # type: ignore
            )
            poll.comment_count += 1
            poll.save()
            serializer = CommentSerializer(comment, many=False)
            if poll_owner == comment.created_by:
                return Response(serializer.data)
            else:
                notification = Notifications.objects.create(
                    type='comment',
                    created_at=datetime.now(),  # type: ignore
                    created_by=request.user,
                    created_for=poll_owner,
                    poll=poll,
                    content=request.data['content']
                )
                notification.save()
                send_noti_comments_poll(poll, comment, poll_owner_fcm_token)
                return Response(serializer.data)
        elif comment_id:
            comment_id = Comment.objects.get(id=comment_id)
            comment_owner = comment_id.created_by
            comment_owner_fcm_token = comment_owner.fcm_token  # type: ignore
            comment = Comment.objects.create(
                parent_id=comment_id,
                created_by=request.user,
                content=request.data['content'],
                created_at=datetime.now()  # type: ignore
            )
            comment_id.reply_count += 1
            comment_id.replies.add(comment)
            comment_id.save()
            serializer = CommentSerializer(comment, many=False)
            if comment_id.created_by == comment.created_by:
                return Response(serializer.data)
            else:
                notification = Notifications.objects.create(
                    type='comment',
                    created_at=datetime.now(),  # type: ignore
                    created_by=request.user,
                    created_for=comment_owner,
                    comment=comment_id,
                    content=request.data['content']
                )
                notification.save()
                send_noti_commets_comments(
                    comment_id, comment, comment_owner_fcm_token)
                return Response(serializer.data)
    else:
        return Response({'detail': 'Post or poll or comment id is required'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def get_comments(request):
    data = request.data
    user_id = request.user.id
    post_id = data.get('post_id')
    poll_id = data.get('poll_id')
    comment_id = data.get('comment_id')
    if post_id or poll_id or comment_id:
        if post_id:
            paginator = MyPagination()
            comments = paginator.paginate_queryset(
                Comment.objects.filter(post_id=post_id).order_by('-created_at'), request)
            serializer = CommentSerializer(
                comments, many=True, context={'request': user_id})
            return paginator.get_paginated_response(serializer.data)
        elif poll_id:
            paginator = MyPagination()
            comments = paginator.paginate_queryset(
                Comment.objects.filter(poll_id=poll_id).order_by('-created_at'), request)
            serializer = CommentSerializer(
                comments, many=True, context={'request': user_id})
            return paginator.get_paginated_response(serializer.data)
        elif comment_id:
            parent_id = Comment.objects.get(id=comment_id)
            paginator = MyPagination()
            comments = paginator.paginate_queryset(
                Comment.objects.filter(parent_id=parent_id).order_by('-created_at'), request)
            serializer = CommentSerializer(
                comments, many=True, context={'request': user_id})
            return paginator.get_paginated_response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def update_comment(request):
    data = request.data
    comment_id = data.get('comment_id')
    if request.user != Comment.objects.get(id=comment_id).created_by:
        return Response({'detail': 'Not authorized to update this comment'}, status=status.HTTP_400_BAD_REQUEST)
    comment = Comment.objects.get(id=comment_id)
    comment.content = data['content']
    comment.save()
    serializer = CommentSerializer(comment, many=False)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def delete_comment(request):
    data = request.data
    comment_id = data.get('comment_id')
    comment = Comment.objects.get(id=comment_id)
    if request.user != comment.created_by:
        return Response({'detail': 'Not authorized to delete this comment'}, status=status.HTTP_400_BAD_REQUEST)
    else:
        comment.delete()
        if comment.post:
            post = comment.post
            post.comment_count -= 1
            post.save()
        elif comment.poll:
            poll = comment.poll
            poll.comment_count -= 1
            poll.save()
        return Response({'detail': 'Comment deleted'}, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def put_like(request):
    data = request.data
    post_id = data.get('post_id')
    poll_id = data.get('poll_id')
    comment_id = data.get('comment_id')
    if post_id or poll_id or comment_id:
        if post_id:
            post = Post.objects.get(id=post_id)
            like = Like.objects.filter(post=post, created_by=request.user)
            post_owner = post.created_by
            post_owner_fcm_token = post_owner.fcm_token  # type: ignore
            if like:
                like.delete()
                post.like_count -= 1
                post.Liked_by.remove(request.user)
                post.save()
                return Response({'message': 'Like Removed', 'is_liked': False})
            else:
                like = Like.objects.create(
                    post=post,
                    created_by=request.user,
                    created_at=datetime.now()  # type: ignore
                )
                post.like_count += 1
                post.Liked_by.add(request.user)
                post.save()
                if post.created_by == request.user:
                    return Response({'message': 'Like Added', 'is_liked': True}, status=status.HTTP_201_CREATED)
                else:
                    notification = Notifications.objects.create(
                        type='like',
                        created_at=datetime.now(),  # type: ignore
                        created_by=request.user,
                        created_for=post_owner,
                        post=post,
                    )
                    notification.save()
                    send_noti_like_post(post, like, post_owner_fcm_token)
                    return Response({'message': 'Like Added', 'is_liked': True}, status=status.HTTP_201_CREATED)
        elif poll_id:
            poll = Poll.objects.get(id=poll_id)
            like = Like.objects.filter(poll=poll, created_by=request.user)
            poll_owner = poll.created_by
            poll_owner_fcm_token = poll_owner.fcm_token  # type: ignore
            if like:
                like.delete()
                poll.like_count -= 1
                poll.liked_by.remove(request.user)
                poll.save()
                return Response({'message': 'Like Removed', 'is_liked': False})
            else:
                like = Like.objects.create(
                    poll=poll,
                    created_by=request.user,
                    created_at=datetime.now()  # type: ignore
                )
                poll.like_count += 1
                poll.liked_by.add(request.user)
                poll.save()
                if poll.created_by == request.user:
                    return Response({'message': 'Like Added', 'is_liked': True})
                else:
                    notification = Notifications.objects.create(
                        type='like',
                        created_at=datetime.now(),  # type: ignore
                        created_by=request.user,
                        created_for=poll_owner,
                        poll=poll,
                    )
                    notification.save()
                    send_noti_like_poll(poll, like, poll_owner_fcm_token)
                    return Response({'message': 'Like Added', 'is_liked': True})
        elif comment_id:
            comment = Comment.objects.get(id=comment_id)
            like = Like.objects.filter(
                comment=comment, created_by=request.user)
            comment_owner = comment.created_by
            comment_owner_fcm_token = comment_owner.fcm_token  # type: ignore
            if like:
                like.delete()
                comment.like_count -= 1
                comment.Liked_by.remove(request.user)
                comment.save()
                return Response({'message': 'Like Removed', 'is_liked': False})
            else:
                like = Like.objects.create(
                    comment=comment,
                    created_by=request.user,
                    created_at=datetime.now()  # type: ignore
                )
                comment.like_count += 1
                comment.Liked_by.add(request.user)
                comment.save()
                if comment.created_by == request.user:
                    return Response({'message': 'Like Added', 'is_liked': True})
                else:
                    notification = Notifications.objects.create(
                        type='like',
                        created_at=datetime.now(),  # type: ignore
                        created_by=request.user,
                        created_for=comment_owner,
                        comment=comment,
                    )
                    notification.save()
                    send_noti_like_comments(
                        comment, like, comment_owner_fcm_token)
                    return Response({'message': 'Like Added', 'is_liked': True})


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_pdf_post(request):

    response = requests.get("http://jmicoe.in/")
    soup = BeautifulSoup(response.content, "html.parser")

    pdf_links = soup.find_all("a", {"href": lambda x: x.endswith(".pdf")})

    pdf_list = []
    for link in pdf_links:
        pdf_list.append(link.get("href"))

    folder_name = "pdfs"
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    for pdf in pdf_list:
        pdf_name = pdf.split("/")[-1]
        if os.path.exists(f"{folder_name}/{pdf_name}"):
            pass

    for pdf in pdf_list:
        pdf_name = pdf.split("/")[-1]

        r = requests.get(pdf, stream=True)
        with open(f"{folder_name}/{pdf_name}", 'wb') as f:
            for chunk in r.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)

    for pdf in pdf_list:
        pdf_name = pdf.split("/")[-1]
        pdf_path = f"{folder_name}/{pdf_name}"
        pages = convert_from_path(pdf_path, 500)
        for page in pages:
            image_name = pdf_name.split(".")[0]
            page.save(f"pdfs/{image_name}.jpg", 'JPEG')

        os.remove(pdf_path)

    for image in os.listdir("pdfs"):
        if image.endswith(".jpg"):
            image_path = f"pdfs/{image}"
            image_name = image.split(".")[0]
            upload_result = cloudinary.uploader.upload(   # type: ignore
                image_path)
            post = Post.objects.create(
                title=image_name,
                content=image_name,
                created_by=Users.objects.get(id=4),
                post_image=upload_result['secure_url'],
                created_at=datetime.now()  # type: ignore
            )

            with open("pdfs/log.txt", "a") as f:
                f.write(f"{image_name}\n")

            os.remove(image_path)

    return Response({'message': 'Post Created'}, status=status.HTTP_201_CREATED)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_all_post_poll(request):
    user = request.user
    paginator = MyPagination()
    posts = Post.objects.all().order_by('-created_at')
    polls = Poll.objects.all().order_by('-created_at')
    poll_options = PollOption.objects.filter(poll__in=polls)
    p = []
    for post in posts:
        if request.user in post.Liked_by.all():
            post.is_liked = True
        else:
            post.is_liked = False
    for poll in polls:
        if request.user in poll.liked_by.all():
            poll.is_liked = True
        else:
            poll.is_liked = False
    for poll in polls:
        if poll.created_by != user and poll.private == True:
            poll.is_voted = poll_options.filter(
                voted_by=user, poll=poll).exists()
            poll.is_liked = poll.liked_by.filter(id=user.id).exists()
            serializer = PostPollSerializer2(poll)
            p.append(serializer.data)
        elif poll.created_by == user:
            poll.is_voted = poll_options.filter(
                voted_by=user, poll=poll).exists()
            poll.is_liked = poll.liked_by.filter(id=user.id).exists()
            serializer = PostPollSerializer(poll)
            p.append(serializer.data)
        elif poll.private == False:
            poll.is_voted = poll_options.filter(
                voted_by=user, poll=poll).exists()
            poll.is_liked = poll.liked_by.filter(id=user.id).exists()
            serializer = PostPollSerializer(poll)
            p.append(serializer.data)

    postserializer = PostPollSerializer(posts, many=True)
    all_post_poll = list(chain(postserializer.data, p))
    all_post_poll.sort(key=lambda x: x['created_at'], reverse=True)
    result_page = paginator.paginate_queryset(all_post_poll, request)
    return paginator.get_paginated_response(result_page)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_notifications(request):
    user = request.user
    notifications = Notifications.objects.filter(
        created_for=user).order_by('-created_at')
    notifications = notifications.filter(created_for=user)
    paginator = MyPagination()
    result_page = paginator.paginate_queryset(notifications, request)
    serializer = NotificationSerializer(result_page, many=True, context={
                                        'notification': notifications})
    return paginator.get_paginated_response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def notification_read(request):
    notification_id = request.data.get('notification_id')
    notification = Notifications.objects.get(id=notification_id)
    notification.is_read = True
    notification.save()
    serializer = NotificationSerializer(notification)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def notification_delete(request):
    notification_id = request.data.get('notification_id')
    notification = Notifications.objects.get(id=notification_id)
    notification.delete()
    return Response({'message': 'Notification Deleted'})


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def delete_all_notifications(request):
    user = request.user
    notifications = Notifications.objects.filter(created_for=user)
    notifications.delete()
    return Response({'message': 'All Notifications Deleted'})


@api_view(['GET'])
def say_hello(request):
    return Response({'message': 'Hello'})
