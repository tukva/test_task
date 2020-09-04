from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    author_name = models.ForeignKey(
        User,
        related_name="posts",
        on_delete=models.SET_NULL,
        null=True,
    )
    title = models.CharField(max_length=120)
    creation_date = models.DateTimeField(auto_now_add=True)
    link = models.URLField()
    upvotes = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.title}"


class Comment(models.Model):
    author_name = models.ForeignKey(
        User,
        related_name="comments",
        on_delete=models.SET_NULL,
        null=True,
    )
    creation_date = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    content = models.TextField(max_length=400, null=True)

    def __str__(self):
        return f"{self.content}"


class Upvote(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name="upvotes", on_delete=models.CASCADE)

    class Meta:
        unique_together = ("post", "user")
