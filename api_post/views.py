from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView
from rest_framework import viewsets
from django.contrib import messages
from django.shortcuts import resolve_url
from django.urls import reverse_lazy
from django.db.models import Q
from rest_framework import authentication, permissions
from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response

from core.models import Post
from .Form import PostForm
from . import serializers
from .serializers import PostSerializer


class CreatePostView(CreateView):
    serializer_class = serializers.PostSerializer
    model = Post
    form_class = PostForm
    success_url = reverse_lazy('')

    def get_success_url(self):
        messages.success(self.request, '投稿しました')
        return resolve_url('')


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)


