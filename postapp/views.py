from user.models import Users
from django.db.models import Q
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from pollapp.models import Poll
from .models import Post, Comment, Like,UserDetails
from .serializers import PostSerializer, CommentSerializer, LikeSerializer,UserDetailsSerializer
from pollapp.paginators import PollPaginator as Paginator
import datetime
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django.contrib.auth.decorators import login_required
from rest_framework.response import Response

@api_view(['GET'])
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


def get_post(request, pk):
    post = Post.objects.get(id=pk)
    serializer = PostSerializer(post, many=False)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_post(request):
    data = request.data
    userdetails = UserDetails.objects.get(user=request.user)
    userdetails.user_post_count += 1
    userdetails.save()
    post = Post.objects.create(
        title=data['title'],
        content=data['content'],
        created_by=request.user,
        created_at=datetime.datetime.now(),
        allow_comments=data['allow_comments']
    )
    serializer = PostSerializer(post, many=False)
    return Response(serializer.data)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_post(request, pk):
    data = request.data
    post = Post.objects.get(id=pk)
    post.title = data['title']
    post.content = data['content']
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
    post.delete()
    return Response('Post Deleted')


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_comment(request, pk):
    data = request.data
    post = Post.objects.get(id=pk)
    comment = Comment.objects.create(
        content=data['content'],
        created_by=request.user,
        post=post
    )
    post.comment_count += 1
    post.save()
    serializer = CommentSerializer(comment, many=False)
    return Response(serializer.data)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_comment(request, pk):
    data = request.data
    comment = Comment.objects.get(id=pk)
    comment.content = data['content']
    comment.last_modified_by = request.user
    comment.last_modified_at = datetime.now()
    comment.save()
    serializer = CommentSerializer(comment, many=False)
    return Response(serializer.data)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_comment(request, pk):
    comment = Comment.objects.get(id=pk)
    comment.delete()
    post = post.objects.get(id=comment.post.id)
    post.comment_count -= 1
    post.save()
    return Response('Comment Deleted')


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getUserDetails(request):
    user =request.user
    user_details = UserDetails.objects.get(user=user)
    user_details.user_posts.set(Post.objects.filter(created_by=user))
    user_details.username = user.username
    user_details.save()
    serializer = UserDetailsSerializer(user_details, many=False)
    return Response(serializer.data)

