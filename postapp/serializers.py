from rest_framework import serializers
from .models import Post, Comment, Like,UserDetails
from pollapp.models import Poll
from datetime import datetime
from user.models import Users as User


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'created_by', 'created_at', 'last_modified_by', 'last_modified_at', 'views',
                  'allow_comments','comment_count','like_count']

   


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"
    
    


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = "__all__"


class UserDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDetails
        fields = ['user','username','user_post_count','user_poll_count','user_posts','user_polls']