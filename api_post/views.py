from django.shortcuts import render
from rest_framework import viewsets, permissions

from core.models import Post
from api_post import serializers

# Create your views here.

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = serializers.PostSerializer
    