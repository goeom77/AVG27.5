from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# Create your models here.
class User(AbstractUser):
    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')
    # nickname = models.CharField(max_length=15, blank=False, null=False)
    profile_img = models.TextField(default='https://assets.repress.co.kr/photos/2009ea104d2c842fed5461308d9f92d7/original.jpg', blank=True)
    # wishlist = models.ManyToManyField(Movie)
    # picklist = models.ManyToManyField(Movie)
    # date_of_birth=models.DateField(default="1992-07-14")
    # last_name=models.CharField(default='ESFJ')
    # followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')
    # pass
    # class Meta:
    #     model = get_user_model()
    #     fields = ('username', 'password', 'first_name','last_name')
# class AddData(models.Model):
#     user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     age = models.IntegerField()
    # mbti = models.choices
