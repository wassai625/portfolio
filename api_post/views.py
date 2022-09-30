from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework import generics
from rest_framework import viewsets

from rest_framework import authentication, permissions

from core.models import Post

from . import serializers
from .serializers import PostSerializer


class CreatePostView(generics.CreateAPIView):
    serializer_class = serializers.PostSerializer
    model = Post


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)


