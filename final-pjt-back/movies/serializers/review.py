from rest_framework import serializers
from django.contrib.auth import get_user_model

from ..models import Review, Movie

class ReviewSerializer(serializers.ModelSerializer):
    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = get_user_model()
            fields = ('pk', 'username')
    user = UserSerializer(read_only=True)
    class Meta:
        model = Review
        fields = ('pk', 'movie', 'user', 'content', 'vote_average','created_at', 'updated_at')
        read_only_fields = ('movie')

