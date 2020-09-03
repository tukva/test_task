from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    author_name = models.ForeignKey(
        User,
        related_name='posts',
        on_delete=models.SET_NULL,
        null=True,
    )
    title = models.CharField(max_length=120)
    creation_date = models.DateTimeField(auto_now_add=True)
    link = models.URLField()
    upvotes = models.IntegerField(default=0)


class Comment(models.Model):
    creation_date = models.DateTimeField(auto_now_add=True)
    author_name = models.ForeignKey(
        User,
        related_name='comments',
        on_delete=models.SET_NULL,
        null=True,
    )
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    parent = models.ForeignKey('Comment', related_name='replies', on_delete=models.CASCADE, null=True, default=None)
    content = models.TextField(null=True)
