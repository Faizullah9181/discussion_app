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



@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_poll(request):
    user = request.user
    data = request.data
    poll = Poll.objects.create(
        title = data['title'],
        content = data['content'],
        created_by = user,
        allow_comments = data['allow_comments']
    )
    poll.save()
    for i in range(1,6):
        if data.get('poll_option'+str(i)):
            poll_option = PollOption.objects.create(
                poll = poll,
                content = data['poll_option'+str(i)]
            )
            poll_option.save()
    # serializer = PollOptionSerializer(poll.polloption_set, many=True)
    return Response('Poll Created', status=status.HTTP_201_CREATED)
    # return Response(serializer.data)

   

