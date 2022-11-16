from .models import Poll, PollOption

from rest_framework import serializers


class PollSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poll
        fields = '__all__'


class PollOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PollOption
        fields = '__all__'

class PollDetailsSerializer(serializers.ModelSerializer):
    poll_options = PollOptionSerializer(read_only= True, many=True)
    class Meta:
        model = Poll
        fields = ['id', 'title', 'created_by', 'created_at', 'allow_comments', 'poll_options']