from django.shortcuts import render
from rest_framework.response import Response
from django.http import HttpResponse, JsonResponse
from django.core import serializers


from .models import Movie
from .serializers.movie import MovieListSerializer
from django.shortcuts import get_list_or_404, get_object_or_404
from rest_framework.decorators import api_view
# Create your views here.

# movie_data 가져오기
@api_view(['GET'])
def movie_list(request):
    movies = get_list_or_404(Movie)
    serializers = MovieListSerializer(movies, many=True)
    # print(serializers.data)
    return Response(serializers.data)



# def article_json_2(request):
#     articles = Article.objects.all()
#     data = serializers.serialize articles)
#     return HttpResponse(data, )