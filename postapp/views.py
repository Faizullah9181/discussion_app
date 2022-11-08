from user.models import Users
from django.db.models import Q
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from pollapp.models import Poll
from .models import Post, Comment, Like,Reply
from user.serializers import UserSerializer
from .serializers import PostSerializer, CommentSerializer, LikeSerializer,ReplySerializer
from pollapp.paginators import PollPaginator as Paginator
import datetime
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django.contrib.auth.decorators import login_required
from rest_framework.response import Response
from datetime import datetime


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user_posts(request, pk):
    posts = Post.objects.filter(created_by=pk)
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_posts(request):
    posts = Post.objects.all()
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_post(request, pk):
    post = Post.objects.get(id=pk)
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
    post.last_modified_at = datetime.now()
    post.allow_comments = data['allow_comments']
    post.save()
    serializer = PostSerializer(post, many=False)
    return Response(serializer.data)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_post(request, pk):
    post = Post.objects.get(id=pk)
    if request.user != post.created_by:
        return Response({'detail': 'Not authorized to delete this post'}, status=status.HTTP_400_BAD_REQUEST)
    post.delete()
    return Response('Post Deleted :(')


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getUserDetails(request):
    user = request.user
    return Response({'user': user.id,
    'username': user.username,
    'user_post_count':Post.objects.filter(created_by=user).count(),
    'user_poll_count':Poll.objects.filter(created_by=user).count(),
    'user_posts':Post.objects.filter(created_by=user).order_by('-created_at')[:5].values_list('id',flat=True),
    'first_name': user.first_name,
    'last_name': user.last_name,
    'user_image': user.image ,
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
    post_id = request.POST.get('post_id')
    poll_id = request.POST.get('poll_id')
    comment_id = request.POST.get('comment_id')
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
            return Response({'id': comment.id, 'post_id': post_id, 
            'like_count':comment.like_count, 'content': comment.content, 
            'created_by': comment.created_by.username, 'created_at': comment.created_at})
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
            return Response({'id': comment.id, 'poll_id': poll_id,
            'like_count':comment.like_count, 'content': comment.content,
            'created_by': comment.created_by.username, 'created_at': comment.created_at})
        elif comment_id:
            comment = Comment.objects.get(id=comment_id)
            reply = Reply.objects.create(
                comment=comment,
                created_by=request.user,
                content=request.data['content'],
                created_at=datetime.now()
            )
            comment.reply_count += 1
            comment.save()
            return Response({'id': reply.id, 'comment_id': comment_id,
            'like_count':reply.like_count, 'content': reply.content,
            'created_by': reply.created_by.username, 'created_at': reply.created_at})

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def get_comments(request):
    post_id = request.POST.get('post_id')
    poll_id = request.POST.get('poll_id')
    comment_id = request.POST.get('comment_id')
    if post_id or poll_id or comment_id:
        if post_id:
            post = Post.objects.get(id=post_id)
            comments = Comment.objects.filter(post=post).order_by('-created_at')
            serializer = CommentSerializer(comments, many=True)
            return Response(serializer.data)
        elif poll_id:
            poll = Poll.objects.get(id=poll_id)
            comments = Comment.objects.filter(poll=poll).order_by('-created_at')
            serializer = CommentSerializer(comments, many=True)
            return Response(serializer.data)
        elif comment_id:
            comment = Comment.objects.get(id=comment_id)
            replies = Reply.objects.filter(comment=comment).order_by('-created_at')
            serializer = ReplySerializer(replies, many=True)
            return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def update_comment(request):
    comment_id = request.POST.get('comment_id')
    reply_id = request.POST.get('reply_id')
    if comment_id or reply_id:
        if comment_id:
            comment = Comment.objects.get(id=comment_id)
            comment.content = request.data['content']
            comment.save()
            return Response({'id': comment.id, 'like_count':comment.like_count, 'content': comment.content, 'created_by': comment.created_by.username, 'created_at': comment.created_at})
        elif reply_id:
            reply = Reply.objects.get(id=reply_id)
            reply.content = request.data['content']
            reply.save()
            return Response({'id': reply.id, 'like_count':reply.like_count, 'content': reply.content, 'created_by': reply.created_by.username, 'created_at': reply.created_at})
        

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_comment(request):
    comment_id = request.POST.get('comment_id')
    reply_id = request.POST.get('reply_id')
    if comment_id or reply_id:
        if comment_id:
            comment = Comment.objects.get(id=comment_id)
            comment.delete()
            return Response('Comment Deleted :(')
        elif reply_id:
            reply = Reply.objects.get(id=reply_id)
            reply.delete()
            return Response('Reply Deleted :(')

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def put_like(request):
    post_id = request.POST.get('post_id')
    poll_id = request.POST.get('poll_id')
    comment_id = request.POST.get('comment_id')
    reply_id = request.POST.get('reply_id')
    if post_id or poll_id or comment_id or reply_id:
        if post_id:
            post = Post.objects.get(id=post_id)
            like = Like.objects.filter(post=post, created_by=request.user)
            if like:
                like.delete()
                post.like_count -= 1
                post.save()
                return Response({'like_count': post.like_count})
            else:
                like = Like.objects.create(
                    post=post,
                    created_by=request.user,
                    created_at=datetime.now()
                )
                post.like_count += 1
                post.save()
                return Response({'like_count': post.like_count})
        elif poll_id:
            poll = Poll.objects.get(id=poll_id)
            like = Like.objects.filter(poll=poll, created_by=request.user)
            if like:
                like.delete()
                poll.like_count -= 1
                poll.save()
                return Response({'like_count': poll.like_count})
            else:
                like = Like.objects.create(
                    poll=poll,
                    created_by=request.user,
                    created_at=datetime.now()
                )
                poll.like_count += 1
                poll.save()
                return Response({'like_count': poll.like_count})
        elif comment_id:
            comment = Comment.objects.get(id=comment_id)
            like = Like.objects.filter(comment=comment, created_by=request.user)
            if like:
                like.delete()
                comment.like_count -= 1
                comment.save()
                return Response({'like_count': comment.like_count})
            else:
                like = Like.objects.create(
                    comment=comment,
                    created_by=request.user,
                    created_at=datetime.now()
                )
                comment.like_count += 1
                comment.save()
                return Response({'like_count': comment.like_count})
        elif reply_id:
            reply = Reply.objects.get(id=reply_id)
            like = Like.objects.filter(reply=reply, created_by=request.user)
            if like:
                like.delete()
                reply.like_count -= 1
                reply.save()
                return Response({'like_count': reply.like_count})
            else:
                like = Like.objects.create(
                    reply=reply,
                    created_by=request.user,
                    created_at=datetime.now()
                )
                reply.like_count += 1
                reply.save()
                return Response({'like_count': reply.like_count})

