from .models import Poll, PollOption
from user.models import Users
from rest_framework import serializers

class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['id', 'username','image']
class PollOptionSerializer(serializers.ModelSerializer):
    voted_by = UserDetailSerializer(many=True, read_only=True)
    class Meta:
        model = PollOption
        fields = ['id','content','votes','voted_by']
class PollSerializer(serializers.ModelSerializer):
    poll_option = serializers.SerializerMethodField()
    class Meta:
        model = Poll
        fields = ['id', 'title', 'content', 'created_at', 'created_by','private' ,'is_voted','total_votes','last_modified_at', 'last_modified_by', 'poll_option','allow_comments', 'comment_count', 'like_count']

    def get_poll_option(self, obj):
        poll_options = PollOption.objects.filter(poll=obj).order_by('id')
        serializer = PollOptionSerializer(poll_options, many=True)
        return serializer.data


    








