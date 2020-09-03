from .models import Post, Upvote


def reset_upvotes():
    posts = Post.objects.all()
    posts.update(upvotes=0)
    Upvote.objects.all().delete()
