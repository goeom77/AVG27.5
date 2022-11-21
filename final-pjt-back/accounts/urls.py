from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    # path('signup/adddata/<str:username>/', views.adddata, name='adddata'),
    path('profile/<str:username>/', views.profile_or_edit, name='profile'),
    path('<int:user>/follow/', views.follow, name='follow'),
    # path('mypage/', views.mypage, name="mypage"),
    # path('<int:user_pk>/', views.user_detail, name="user_detail"),
    # path('delete/', views.user_delete, name="user_delete"),
    # path('<int:user_pk>/follow/', views.follow, name="follow"),
]