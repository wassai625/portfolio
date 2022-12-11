from rest_framework import serializers

from core.models import Post
from api_user.serializers import UserSerializer

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('writer', 'title', 'text', 'created_at')

class PostWithForeignSerializer(serializers.ModelSerializer):
    user = UserSerializer

    class Meta:
        model = Post
        fields = ('id', 'user', 'title', 'writer', 'text',)
