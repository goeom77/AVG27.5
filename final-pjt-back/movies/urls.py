from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('', views.movie_list),
    path('<int:movie_pk>/review/', views.review_list_create),
    path('<int:movie_pk>/review/<int:review_pk>/', views.review_detail),
]

