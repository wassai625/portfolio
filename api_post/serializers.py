from rest_framework import serializers

from core.models import Post, PostComment, User

class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ('writer', 'title', 'text', 'created_at')


class PostCommentWithForeignSerializer(serializers.ModelSerializer):
    post = PostSerializer()
    user = PostSerializer()

    class Meta:
        model = PostComment
        fields = ('id', 'user', 'post', 'comment_text', 'comment_data', 'tweet_flag', 'delete_flag',)

