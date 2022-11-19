from django.contrib.auth import get_user_model
from rest_framework import serializers
User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ('username', 'first_name','last_name')

class ProfileUserSerializer(serializers.ModelSerializer):
    # followers = UserSerializer(many=True, read_only=True)
    
    class Meta:
        model = User
        fields = ('username', 'first_name','last_name')

# class UserSimpleSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         exclude = ('nickname',)


# class CustomRegisterSerializer(RegisterSerializer):
#     username = serializers.CharField(required=True, write_only=True)
#     password1 = serializers.CharField(required=True, write_only=True)
#     password2 = serializers.CharField(required=True, write_only=True)
#     email = serializers.CharField(required=True)
#     nickname = serializers.CharField(required=True)


# class UserIdSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = get_user_model()
#         fields = ['id']