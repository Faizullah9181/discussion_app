from rest_framework import serializers
from .models import Post, Comment, Like, UserDetails, Notifications
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


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = "__all__"


class CommentSerializer(serializers.ModelSerializer):
    created_by = UserDetailSerializer(read_only=True)
    replies = serializers.SerializerMethodField()
    is_liked = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = ('id', 'content', 'created_at', 'created_by', 'is_liked', 'like_count',
                  'last_modified_at', 'reply_count', 'parent_id', 'replies')

    def get_is_liked(self, obj):
        user_id = self.context.get("request")
        if obj.id:
            return Comment.Liked_by.through.objects.filter(comment_id=obj.id, users_id=user_id).exists()
        else:
            return Comment.Liked_by.through.objects.filter(comment_id=obj.id, users_id=user_id).exists()

    def get_replies(self, obj):
        replies = Comment.objects.filter(parent_id=obj.id).order_by('-id')
        serializer = CommentSerializer(
            replies, many=True, context=self.context)
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
        fields = ['id', 'content', 'votes', 'voted_by']


class PollOptionSerializer2(serializers.ModelSerializer):
    voted_by = EmptyArrayField()

    class Meta:
        model = PollOption
        fields = ['id', 'content', 'votes', 'voted_by']


class PollSerializer(serializers.ModelSerializer):
    poll_option = serializers.SerializerMethodField()
    created_by = UserDetailSerializer(read_only=True)

    class Meta:
        model = Poll
        fields = ['id', 'title', 'content', 'created_at', 'created_by', 'private', 'is_voted', 'is_liked', 'total_votes',
                  'last_modified_at', 'last_modified_by', 'poll_option', 'allow_comments', 'comment_count', 'like_count']

    def get_poll_option(self, obj):
        poll_options = PollOption.objects.filter(poll=obj).order_by('id')
        serializer = PollOptionSerializer(poll_options, many=True)
        return serializer.data


class PollSerializer2(serializers.ModelSerializer):
    poll_option = serializers.SerializerMethodField()
    created_by = UserDetailSerializer()

    class Meta:
        model = Poll
        fields = ['id', 'title', 'content', 'created_at', 'created_by', 'private', 'is_liked', 'is_voted', 'total_votes',
                  'last_modified_at', 'last_modified_by', 'poll_option', 'allow_comments', 'comment_count', 'like_count']

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





class PostSerializerForNotifications(serializers.ModelSerializer):
    created_by = UserDetailSerializer(read_only=True)
    comment = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'created_by',
             'created_at', 'post_image', 'comment']

    def get_comment(self, obj):
        notification = Notifications.objects.filter(post=obj, type='comment').order_by('-id')
        if notification.exists():
            return notification.first().content
        return None


class PollSerializerForNotifications(serializers.ModelSerializer):
    created_by = UserDetailSerializer(read_only=True)
    comment = serializers.SerializerMethodField()

    class Meta:
        model = Poll
        fields = ['id', 'title', 'content', 'created_by', 'created_at', 'comment']
    
    def get_comment(self, obj):
        notification = Notifications.objects.filter(poll=obj, type='comment').order_by('-id')
        if notification.exists():
            return notification.first().content
        return None


class CommentSerializerForNoti(serializers.ModelSerializer):
    created_by = UserDetailSerializer(read_only=True)
    comment = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields =[ 'id', 'content', 'created_at', 'created_by' , 'comment' , 'poll', 'post']
    
    def get_comment(self, obj):
        notification = Notifications.objects.filter(comment=obj, type='comment').order_by('-id')
        if notification.exists():
            return notification.first().content
        return None

class NotificationSerializer(serializers.ModelSerializer):
    created_by = UserDetailSerializer(read_only=True)
    post = PostSerializerForNotifications(read_only=True)
    poll = PollSerializerForNotifications(read_only=True)
    comment = CommentSerializerForNoti(required=False)

    class Meta:
        model = Notifications
        fields = ['id', 'created_by', 'created_at', 'is_read',
                  'type', 'post', 'poll', 'comment', 'created_for']
    
    def to_representation(self, instance):
        data = super().to_representation(instance)
        if instance.type == 'comment':
            if instance.post:
                data['post']['comment'] = instance.content
            elif instance.poll:
                data['poll']['comment'] = instance.content
            elif instance.comment:
                data['comment']['comment'] = instance.content
        return data


class NotificationSerializer2(serializers.ModelSerializer):
    created_by = UserDetailSerializer(read_only=True)
    post = PostSerializerForNotifications(read_only=True)
    poll = PollSerializerForNotifications(read_only=True)
    comment = CommentSerializerForNoti(required=False)

    class Meta:
        model = Notifications
        fields = ['id', 'created_by', 'created_at', 'is_read',
                  'type', 'post', 'poll', 'comment', 'created_for']



