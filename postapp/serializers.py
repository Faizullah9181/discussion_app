from rest_framework import serializers
from .models import Post, Comment, Like,UserDetails,Reply
from pollapp.models import Poll
from datetime import datetime
from user.models import Users
from django.db.models import Q
from user.serializers import UserSerializer



class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['id', 'username','image']

class PostSerializer(serializers.ModelSerializer):
    created_by = UserDetailSerializer(read_only=True)
    id = serializers.IntegerField(read_only=True)
    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'created_by', 'created_at', 'post_image','last_modified_by', 'last_modified_at', 'views',
                  'allow_comments','is_liked','comment_count','like_count']

    def get_post_id(self, obj):
        #post always in sorted order by id in increasing order
        id = Post.objects.filter(Q(created_by=obj.created_by) & Q(created_at__lte=obj.created_at)).count()
        return id






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


