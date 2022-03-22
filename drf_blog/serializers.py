from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Post, Vote


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['title', 'url', 'poster', 'create']

