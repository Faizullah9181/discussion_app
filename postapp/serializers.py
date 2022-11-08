from rest_framework import serializers
from .models import Post, Comment, Like,UserDetails,Reply
from pollapp.models import Poll
from datetime import datetime
from user.models import Users as User
from django.db.models import Q


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'created_by', 'created_at', 'post_image','last_modified_by', 'last_modified_at', 'views',
                  'allow_comments','comment_count','like_count']

   


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"

    
class ReplySerializer(serializers.ModelSerializer):
    class Meta:
        model = Reply
        fields = "__all__"
    
    


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = "__all__"


class UserDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDetails
        fields = ['user','username','user_post_count','user_poll_count','user_posts','first_name','last_name','user_image']







"""
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

"""


