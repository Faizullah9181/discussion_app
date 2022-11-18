from .models import Poll, PollOption

from rest_framework import serializers

class PollSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poll
        fields = ['id', 'title', 'content', 'created_at', 'created_by', 'last_modified_at', 'last_modified_by', 'allow_comments', 'comment_count', 'like_count']






class PollOptionSerializer(serializers.ModelSerializer):
    poll = PollSerializer(many=False, read_only=True)
    class Meta:
        model = PollOption
        fields = ['id','poll','content','votes','voted_by']


