# Generated by Django 3.2.12 on 2022-11-22 07:11

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('movies', '0002_review_liked_users'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='pickuser',
            field=models.ManyToManyField(blank=True, related_name='pickmovies', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='movie',
            name='wishuser',
            field=models.ManyToManyField(blank=True, related_name='wishmovies', to=settings.AUTH_USER_MODEL),
        ),
    ]
