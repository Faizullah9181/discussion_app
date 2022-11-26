from django.shortcuts import render
from .models import Poll, PollOption
from .serializers import PollSerializer , PollSerializer2
from rest_framework import generics
from rest_framework import permissions
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from user.models import Users
from django.db.models import Q
from postapp.models import Post, Comment, Like
from postapp.serializers import PostSerializer, CommentSerializer, LikeSerializer
from user.serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from datetime import datetime
import json
from django.http import JsonResponse

def is_voted(poll, user):
    poll_options = PollOption.objects.filter(poll=poll)
    for poll_option in poll_options:
        if user in poll_option.voted_by.all():
            return True
    return False




    

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_poll(request):
    user = request.user
    data = request.data
    poll = Poll.objects.create(
        title=data['title'],
        content=data['content'],
        created_by=user,
        created_at=datetime.now(),
        last_modified_by=user,
        last_modified_at=datetime.now(),
        allow_comments=data['allow_comments'],
        private = data['private']
    )
    poll.save()
    for i in range(1, 7):
        if data.get('poll_option'+str(i)):
            poll_option = PollOption.objects.create(
                poll=poll,
                content=data['poll_option'+str(i)]
            )
            poll_option.save()
    serializer = PollSerializer(poll)
    return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_poll(request, poll_id):
    user = request.user
    poll = Poll.objects.get(id=poll_id)
    poll_options = PollOption.objects.filter(poll=poll)
    poll.is_liked = user in poll.liked_by.all()
    for poll_option in poll_options:
        if user in poll_option.voted_by.all():
            poll.is_voted = True
            break
    if poll.created_by != user and poll.private == True:
        serializer = PollSerializer2(poll)
    else:
        serializer = PollSerializer(poll)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user_polls(request):
    user = request.user
    polls = Poll.objects.filter(created_by=user)
    poll_options = PollOption.objects.filter(poll__in=polls)
    for poll in polls:
        poll.is_voted = is_voted(poll, user)
        poll.is_liked = user in poll.liked_by.all()
    serializer = PollSerializer(polls, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

    
    
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def delete_poll(request, poll_id):
    user = request.user
    poll = Poll.objects.get(id=poll_id)
    if poll.created_by == user:
        poll.delete()
        return Response({'message': 'Poll deleted successfully'}, status=status.HTTP_200_OK)
    else:
        return Response({'message': 'You are not authorized to delete this poll'}, status=status.HTTP_401_UNAUTHORIZED)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_all_polls(request):
    user = request.user
    polls = Poll.objects.all()
    poll_options = PollOption.objects.filter(poll__in=polls)
    p = []
    for poll in polls:
        if poll.created_by != user and poll.private == True:
            poll.is_voted = poll_options.filter(voted_by=user, poll=poll).exists()
            poll.is_liked = poll.liked_by.filter(id=user.id).exists()
            serializer = PollSerializer2(poll)
            p.append(serializer.data)
        elif poll.created_by == user:
            poll.is_voted = poll_options.filter(voted_by=user, poll=poll).exists()
            poll.is_liked = poll.liked_by.filter(id=user.id).exists()
            serializer = PollSerializer(poll)
            p.append(serializer.data)
        elif poll.private == False:
            poll.is_voted = poll_options.filter(voted_by=user, poll=poll).exists()
            poll.is_liked = poll.liked_by.filter(id=user.id).exists()
            serializer = PollSerializer(poll)
            p.append(serializer.data)
    return Response(p, status=status.HTTP_200_OK)

# def get_all_polls(request):
#     user = request.user
#     polls = Poll.objects.all()
#     poll_options = PollOption.objects.filter(poll__in=polls)
#     p = []
#     for poll in polls:
#         if poll.created_by != user and poll.private == True:
#             for poll_option in poll_options:
#                 if user in poll_option.voted_by.all():
#                     poll.is_voted = True
#             serializer = PollSerializer2(poll)
#             p.append(serializer.data)
#         elif poll.created_by == user:
#             for poll_option in poll_options:
#                 if user in poll_option.voted_by.all():
#                     poll.is_voted = True
#             serializer = PollSerializer(poll)
#             p.append(serializer.data)
#         elif poll.private == False:
#             for poll_option in poll_options:
#                 if user in poll_option.voted_by.all():
#                     poll.is_voted = True
#             serializer = PollSerializer(poll)
#             p.append(serializer.data)
#     return Response(p, status=status.HTTP_200_OK)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def vote_poll(request):
    user = request.user
    data = request.data
    poll = Poll.objects.get(id=data['poll_id'])
    poll_options = PollOption.objects.filter(poll=poll)
    if not poll_options.filter(id=data['poll_option_id']).exists():
        return Response({'message': 'Invalid poll option'}, status=status.HTTP_404_NOT_FOUND)
    for poll_option in poll_options:
        if user in poll_option.voted_by.all():
            return Response({'message': 'You have already voted for this poll'}, status=status.HTTP_401_UNAUTHORIZED)
    poll_option = PollOption.objects.get(id=data['poll_option_id'])
    poll.is_liked = user in poll.liked_by.all()
    poll.total_votes += 1
    poll.save()
    poll_option.voted_by.add(user)
    for poll_option in poll_options:
        if user in poll_option.voted_by.all():
            poll.is_voted = True
    for poll_option in poll_options:
        poll_option.votes = poll_option.voted_by.count()
        poll_option.save()
    if poll.created_by != user and poll.private == True:
        serializer = PollSerializer2(poll)
    else:
        serializer = PollSerializer(poll)
    return Response(serializer.data, status=status.HTTP_200_OK)




