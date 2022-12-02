from .models import Poll, PollOption
from user.models import Users
from rest_framework import serializers
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes

class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['id', 'username','image']

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
   
    
    






