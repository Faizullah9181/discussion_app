from django.shortcuts import render
from .models import Poll, PollOption
from .serializers import PollSerializer, PollOptionSerializer
from rest_framework import generics
from rest_framework import permissions
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from user.models import Users
from django.db.models import Q
from postapp.models import Post,Comment,Like
from postapp.serializers import PostSerializer,CommentSerializer,LikeSerializer
from user.serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from datetime import datetime


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_polls(request):
    polls = Poll.objects.all()
    serializer = PollSerializer(polls, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_poll(request):
    data = request.data
    poll = Poll.objects.create(
        title=data['title'],
        created_by=request.user,
        allow_comments=data['allow_comments'],
        created_at=datetime.now(),
    )
    serializer = PollSerializer(poll, many=False)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_poll_option(request):
    data = request.data
    poll_id = request.POST.get('poll_id')
    poll = Poll.objects.get(id=poll_id)
    poll_option = PollOption.objects.create(
        poll=poll,
        content=data['content'],
    )
    serializer = PollOptionSerializer(poll_option, many=False)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def vote_poll(request):
    data =request.data
    poll_id = request.POST.get('poll_id')
    poll_option_id = request.POST.get('poll_option_id')
    poll = Poll.objects.get(id=poll_id)
    poll_option = PollOption.objects.get(id=poll_option_id)
    # poll_option.votes += 1
    # poll_option.voted_by.add(request.user)
    if request.user in poll_option.voted_by.all():
        poll_option.votes -= 1
        poll_option.voted_by.remove(request.user)
    else:
        poll_option.votes += 1
        poll_option.voted_by.add(request.user)
    poll_option.save()
    serializer = PollOptionSerializer(poll_option, many=False)
    return Response(serializer.data)
    