from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.shortcuts import get_object_or_404, get_list_or_404
from django.contrib.auth import get_user_model
from django.http import HttpResponse
from .serializers import ProfileUserSerializer


# Create your views here.

def profile(request, username):
    user = get_object_or_404(get_user_model(), username=username)

    if request.method == 'GET':
        serializer = ProfileUserSerializer(user)
        return HttpResponse(serializer.data)
    
    # elif request.method == 'PUT':
    #     user = get_user_model()
    #     serializer = ProfileUserSerializer(user, data=request.data)
    #     if serializer.is_valid(raise_exception=True):
    #         serializer.save()
    #         return Response(serializer.data)