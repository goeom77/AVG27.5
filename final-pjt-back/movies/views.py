from django.shortcuts import render
from rest_framework.response import Response
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from rest_framework import status

from .models import Movie, Review
from .serializers.movie import MovieListSerializer, MovieSerializer
from .serializers.review import ReviewListSerializer, ReviewSerializer
from django.shortcuts import get_list_or_404, get_object_or_404
from rest_framework.decorators import api_view
# Create your views here.

# movie_data 가져오기
@api_view(['GET'])
def movie_list(request):
    movies = get_list_or_404(Movie)
    serializers = MovieListSerializer(movies, many=True)
    return Response(serializers.data)

@api_view(['GET','POST'])
def review_list_create(request, movie_pk):
    if request.method == 'GET':
        reviews = get_list_or_404(Review, movie_id=movie_pk)
        serializer = ReviewListSerializer(reviews, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'DELETE', 'PUT'])
def review_detail(request, movie_pk, review_pk):
    review = get_object_or_404(Review, pk=review_pk)

    if request.method == 'GET':
        serializer = ReviewSerializer(review)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        review.delete()
        reviews = get_list_or_404(Review, movie_id=movie_pk)
        serializer = ReviewListSerializer(reviews, many=True)
        return Response(serializer.data)
        
    elif request.method == 'PUT':
        serializer = ReviewSerializer(review, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

@api_view(['GET', 'POST'])
def review_like(request, movie_pk, review_pk):
    user = request.user
    review = get_object_or_404(Review, pk=review_pk)
    if request.method == 'GET':
        if user in review.like_users.all():
            liked = True
        else:
            liked = False
        context = {
            'liked': liked,
            'count': review.like_users.count()
        }
        return Response(context)
    elif request.method == 'POST':
        if user in review.like_users.all():
            review.like_users.remove(user)
            liked = False
        else:
            review.like_users.add(user)
            liked = True
        context = {
            'liked': liked,
            'count': review.like_users.count()
        }
        return Response(context)

@api_view(['POST'])
def wish_movies(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    user = request.user
    if movie.wishuser.filter(pk=user.pk).exists():
        movie.wishuser.remove(user)
        
    else:
        movie.wishuser.add(user)
    serializer = MovieSerializer(movie)
    return Response(serializer.data)

@api_view(['POST'])
def pick_movies(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    user = request.user
    if movie.pickuser.filter(pk=user.pk).exists():
        movie.pickuser.remove(user)
    else:
        movie.pickuser.add(user)
    serializer = MovieSerializer(movie)
    return Response(serializer.data)