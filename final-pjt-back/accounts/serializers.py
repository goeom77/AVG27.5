# from rest_framework import serializers
# from django.contrib.auth import get_user_model
# from .models import AddData

# User = get_user_model()

# class UserSerializer(serializers.ModelSerializer):
    
#     class Meta:
#         model = User
#         exclude = ['password']

# class ProfileUserSerializer(serializers.ModelSerializer):
#     followers = UserSerializer(many=True, read_only=True)
from rest_framework import serializers
from django.contrib.auth import get_user_model
# from movies.models import Movie
# from community.models import Article
from dj_rest_auth.registration.serializers import RegisterSerializer

class ProfileSerializer(serializers.ModelSerializer):
    
    #유저가 좋아요한 게시글들, 유저가 작성한 게시글을 가져오기 위해 재정의
    # class ArticleSerializer(serializers.ModelSerializer):
        
    #     class Meta:
    #         model = Article
    #         fields = '__all__'

    #유저가 팔로우한 영화들을 가져오기 위해 재정의
    # class MovieFollowSerializer(serializers.ModelSerializer):
        
    #     class Meta:
    #         model = Movie
    #         fields = '__all__'
        
    # 유저가 좋아요한 게시글 / 유저가 작성한 게시글 / 유저가 팔로우한 영화들
    # like_articles = ArticleSerializer(many=True, read_only=True)
    # articles = ArticleSerializer(many=True, read_only=True)
    # keep_movies = MovieFollowSerializer(many=True, read_only=True)
    class Meta:
        model = get_user_model()
        fields = ('pk', 'username', 'email', 'followings', 'followers', 'profile_img')
        read_only_fields = ('followings', 'followers')

class CustomSignupSerializer(RegisterSerializer):
    profile_img = serializers.CharField(min_length=0)
    # genre_likes = serializers.JSONField(default=dict)
    def get_cleaned_data(self):
        data = super().get_cleaned_data()
        data['profile_img'] = self.validated_data.get('profile_img', '')
        # data['genre_likes'] = self.validated_data.get('genre_likes', '')

        return data