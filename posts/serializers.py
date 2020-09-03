from .models import Post, Comment, Upvote
from rest_framework import serializers


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['author_name', 'title', 'creation_date', 'link', 'upvotes']


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['author_name', 'creation_date', 'post', 'content']


class UpvoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Upvote
        fields = ['post', 'user']
