from rest_framework import serializers
from .models import Post, Comentari
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'subtitle', 'text', 'begin_date', 'photo', 'active', 'user']

class ComentariSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comentari
        fields = ['post', 'text', 'begin_date', 'active', 'user']



