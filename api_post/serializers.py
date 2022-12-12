from rest_framework import serializers

from core.models import Post,PostComment
from api_user.serializers import UserSerializer

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('writer', 'title', 'text', 'created_at')

class PostWithForeignSerializer(serializers.ModelSerializer):
    user = UserSerializer
    class Meta:
        model = Post
        fields = '__all__'

class PostCommentWithForeignSerializer(serializers.ModelSerializer):
    post = serializers.SerializerMethodField
    class Meta:
        model = PostComment
        fields = ('id', 'user', 'post', 'comment_text', 'comment_data',)

    def create(self, validated_data):
        return Post(**validated_data)


