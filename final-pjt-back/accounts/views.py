from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.contrib.auth import get_user_model
from .serializers import ProfileSerializer, UserInfoSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status



@api_view(['GET', 'PUT'])
def profile_or_edit(request, username):

    user = get_object_or_404(get_user_model(), username=username)
    if request.method == 'GET':
        serializer = ProfileSerializer(user)
        print(serializer)
        return Response(serializer.data)
    
    elif request.user.is_authenticated:
        serializer = ProfileSerializer(data=request.data, instance=user)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        
@api_view(['POST'])
def follow(request, user_pk):
    you = get_object_or_404(get_user_model(), pk=user_pk)
    me = request.user

    if you.followers.filter(pk=me.pk).exists():
        # 언팔로우
        print('unfollow')
        you.followers.remove(me)
        serializer = ProfileSerializer(you)
        return Response(serializer.data)
    else:
        # 팔로우
        print('follow로 들어옴')
        you.followers.add(me)
        serializer = ProfileSerializer(you)
        return Response(serializer.data)

@api_view(['GET'])
def users(request):
    users = get_list_or_404(get_user_model())
    # users.remove(request.pk)
    serializer = ProfileSerializer(users, many=True)
    return Response(serializer.data)
