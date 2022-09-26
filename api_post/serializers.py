from rest_framework import serializers
from core.models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'writer', 'title', 'text')

    def create(self, validated_data):
        post = Post.objects.create_post(**validated_data)
        return post
