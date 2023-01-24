from itertools import chain
from operator import attrgetter
import os
from user.models import Users
from rest_framework.response import Response
from rest_framework import status
from pollapp.models import Poll
from .models import Post, Comment, Like
from .serializers import PostSerializer, CommentSerializer, PostPollSerializer, PollOptionSerializer2
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
from rest_framework.pagination import PageNumberPagination
from django.db.models import Q


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user_posts(request, pk):
    posts = Post.objects.filter(created_by=pk).order_by('-id')
    for post in posts:
        if post.Liked_by.filter(id=request.user.id).exists():
            post.is_liked = True
        else:
            post.is_liked = False
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_posts(request):
    posts = Post.objects.all().order_by('-id')
    for post in posts:
        if post.Liked_by.filter(id=request.user.id).exists():
            post.is_liked = True
        else:
            post.is_liked = False
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)


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
        created_at=datetime.now(),
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
    post.last_modified_at = datetime.now()
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
    user = request.user
    return Response({'user': user.id,
                     'username': user.username,
                     'user_post_count': Post.objects.filter(created_by=user).count(),
                     'user_poll_count': Poll.objects.filter(created_by=user).count(),
                     # 'user_posts':Post.objects.filter(created_by=user).order_by('-created_at')[:5].values_list('id',flat=True)
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
            comment = Comment.objects.create(
                post=post,
                created_by=request.user,
                content=request.data['content'],
                created_at=datetime.now()
            )
            post.comment_count += 1
            post.save()
            serializer = CommentSerializer(comment, many=False)
            return Response(serializer.data)
        elif poll_id:
            poll = Poll.objects.get(id=poll_id)
            comment = Comment.objects.create(
                poll=poll,
                created_by=request.user,
                content=request.data['content'],
                created_at=datetime.now()
            )
            poll.comment_count += 1
            poll.save()
            serializer = CommentSerializer(comment, many=False)
            return Response(serializer.data)
        elif comment_id:
            comment_id = Comment.objects.get(id=comment_id)
            comment = Comment.objects.create(
                parent_id=comment_id,
                created_by=request.user,
                content=request.data['content'],
                created_at=datetime.now()
            )
            comment_id.reply_count += 1
            comment_id.replies.add(comment)
            comment_id.save()
            serializer = CommentSerializer(comment, many=False)
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
            post = Post.objects.get(id=post_id)
            comments = Comment.objects.filter(post=post).order_by('-created_at')
            serializer = CommentSerializer(
                comments, many=True, context={'request': user_id})
            return Response(serializer.data)
        elif poll_id:
            poll = Poll.objects.get(id=poll_id)
            comments = Comment.objects.filter(poll=poll).order_by('-created_at')
            serializer = CommentSerializer(comments, many=True , context={'request': user_id})
            return Response(serializer.data)
        elif comment_id:
            parent_id = Comment.objects.get(id=comment_id)
            comments = Comment.objects.filter(parent_id=parent_id).order_by('-created_at')
            serializer = CommentSerializer(comments, many=True , context={'request': user_id})
            return Response(serializer.data)


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
                    created_at=datetime.now()
                )
                post.like_count += 1
                post.Liked_by.add(request.user)
                post.save()
                return Response({'message': 'Like Added', 'is_liked': True}, status=status.HTTP_201_CREATED)
        elif poll_id:
            poll = Poll.objects.get(id=poll_id)
            like = Like.objects.filter(poll=poll, created_by=request.user)
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
                    created_at=datetime.now()
                )
                poll.like_count += 1
                poll.liked_by.add(request.user)
                poll.save()
                return Response({'message': 'Like Added', 'is_liked': True})
        elif comment_id:
            comment = Comment.objects.get(id=comment_id)
            like = Like.objects.filter(
                comment=comment, created_by=request.user)
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
                    created_at=datetime.now()
                )
                comment.like_count += 1
                comment.Liked_by.add(request.user)
                comment.save()
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
            upload_result = cloudinary.uploader.upload(image_path)
            post = Post.objects.create(
                title=image_name,
                content=image_name,
                created_by=Users.objects.get(id=1),
                post_image=upload_result['secure_url'],
                created_at=datetime.now()
            )

            with open("pdfs/log.txt", "a") as f:
                f.write(f"{image_name}\n")

            os.remove(image_path)

    return Response({'message': 'Post Created'}, status=status.HTTP_201_CREATED)


class MyPagination(PageNumberPagination):
    page_size = 100


@api_view(['GET'])
def get_all_post_poll(request):
    posts = Post.objects.all().order_by('-created_at')
    polls = Poll.objects.all().order_by('-created_at')
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
    all_post_poll = list(chain(posts, polls))
    all_post_poll.sort(key=lambda x: x.created_at, reverse=True)
    paginator = MyPagination()
    result_page = paginator.paginate_queryset(all_post_poll, request)
    serializer = PostPollSerializer(result_page, many=True)
    return paginator.get_paginated_response(serializer.data)
