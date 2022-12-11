from rest_framework import viewsets, permissions, generics

from api_post import serializers
from core.models import Post


# Create your views here.

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = serializers.PostSerializer


class PostListView(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = serializers.PostWithForeignSerializer

    def get_queryset(self):
        queryset = Post.objects.all()
        title = self.request.query_params.get('title', None)
        if title is not None:
            queryset = queryset.filter(post__title__icontains=title)
        return queryset
