from rest_framework import serializers
from .models import Post, Comment, Like, UserDetails, Reply
from pollapp.models import Poll, PollOption
from datetime import datetime
from user.models import Users
from django.db.models import Q
from user.serializers import UserSerializer


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['id', 'username', 'image']


class PostSerializer(serializers.ModelSerializer):
    created_by = UserDetailSerializer(read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'created_by', 'created_at', 'post_image', 'last_modified_by', 'last_modified_at', 'views',
                  'allow_comments', 'is_liked', 'comment_count', 'like_count']


class ReplySerializer(serializers.ModelSerializer):
    created_by = UserDetailSerializer(read_only=True)

    class Meta:
        model = Reply
        fields = ["id", "content", "created_at", "created_by", "comment_id"]


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = "__all__"


class CommentSerializer(serializers.ModelSerializer):
    reply = serializers.SerializerMethodField()
    created_by = UserDetailSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = ["id", "content", "created_at", "created_by",
              "reply"]

    def get_reply(self, obj):
        reply = Reply.objects.filter(comment=obj).order_by('-created_at')
        serializer = ReplySerializer(reply, many=True)
        return serializer.data

class EmptyArrayField(serializers.Field):
    def to_representation(self, value):
        return []

    def to_internal_value(self, data):
        return []

class PollOptionSerializer(serializers.ModelSerializer):

    voted_by = UserDetailSerializer(many=True, read_only=True)
    class Meta:
        model = PollOption
        fields = ['id','content','votes','voted_by']


class PollOptionSerializer2(serializers.ModelSerializer):
    voted_by = EmptyArrayField()
    class Meta:
        model = PollOption
        fields = ['id','content','votes','voted_by']


class PollSerializer(serializers.ModelSerializer):
    poll_option = serializers.SerializerMethodField()
    created_by = UserDetailSerializer(read_only=True)
    class Meta:
        model = Poll
        fields = ['id', 'title', 'content', 'created_at', 'created_by','private' ,'is_voted','is_liked','total_votes','last_modified_at', 'last_modified_by', 'poll_option','allow_comments', 'comment_count', 'like_count']

    def get_poll_option(self, obj):
        poll_options = PollOption.objects.filter(poll=obj).order_by('id')
        serializer = PollOptionSerializer(poll_options, many=True)
        return serializer.data

class PollSerializer2(serializers.ModelSerializer):
    poll_option = serializers.SerializerMethodField()
    created_by = UserDetailSerializer()

    class Meta:
        model = Poll
        fields = ['id', 'title', 'content', 'created_at', 'created_by','private', 'is_liked','is_voted','total_votes','last_modified_at', 'last_modified_by', 'poll_option','allow_comments', 'comment_count', 'like_count']

    def get_poll_option(self, obj):
        poll_options = PollOption.objects.filter(poll=obj).order_by('id')
        serializer = PollOptionSerializer2(poll_options, many=True)
        return serializer.data


class PostPollSerializer(serializers.ModelSerializer):
    created_by = UserDetailSerializer(read_only=True)
   
    poll = PollSerializer(required=False)

    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'created_by', 'created_at', 'post_image', 'last_modified_by', 'last_modified_at', 'views',
                  'allow_comments', 'is_liked', 'comment_count', 'like_count', 'poll']  # include the 'poll' field

    def to_representation(self, instance):
        if isinstance(instance, Post):
            return super().to_representation(instance)
        elif isinstance(instance, Poll):
            return PollSerializer(instance).data


class PostPollSerializer2(serializers.ModelSerializer):
    created_by = UserDetailSerializer(read_only=True)
    poll = PollSerializer2(required=False)

    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'created_by', 'created_at', 'post_image', 'last_modified_by', 'last_modified_at', 'views',
                  'allow_comments', 'is_liked', 'comment_count', 'like_count', 'poll']  # include the 'poll' field

    def to_representation(self, instance):
        if isinstance(instance, Post):
            return super().to_representation(instance)
        elif isinstance(instance, Poll):
            return PollSerializer2(instance).data


