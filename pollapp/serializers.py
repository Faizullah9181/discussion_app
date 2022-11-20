from .models import Poll, PollOption

from rest_framework import serializers


class PollOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PollOption
        fields = ['id','content','votes','voted_by']


class PollSerializer(serializers.ModelSerializer):
    poll_option = serializers.SerializerMethodField()
    class Meta:
        model = Poll
        fields = ['id', 'title', 'content', 'created_at', 'created_by', 'last_modified_at', 'last_modified_by', 'poll_option','allow_comments', 'comment_count', 'like_count']

    def get_poll_option(self, obj):
        poll_option = PollOption.objects.filter(poll=obj)
        serializer = PollOptionSerializer(poll_option, many=True)
        return serializer.data







