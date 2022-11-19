from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.contrib.auth import get_user_model

# Create your models here.
class User(AbstractUser):
    # followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')
    
    # class Meta:
    #     model = get_user_model()
    #     fields = ('username', 'password', 'first_name','last_name')
    pass