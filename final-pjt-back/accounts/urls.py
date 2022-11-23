from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    # path('signup/adddata/<str:username>/', views.adddata, name='adddata'),
    path('profile/<str:username>/', views.profile_or_edit, name='profile'),
    path('<str:username>/follow/', views.follow, name='follow'),
    path('users/', views.users, name='users'),
    path('profile/<int:user_pk>/', views.usersearch,),
    # path('mypage/', views.mypage, name="mypage"),
    # path('<int:user_pk>/', views.user_detail, name="user_detail"),
    # path('delete/', views.user_delete, name="user_delete"),
    # path('<int:user_pk>/follow/', views.follow, name="follow"),
]