from rest_framework import viewsets, views, status
from rest_framework.response import Response
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer, UpvoteSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by("-creation_date")
    serializer_class = PostSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all().order_by("-creation_date")
    serializer_class = CommentSerializer


class UpvoteList(views.APIView):
    def post(self, request):
        serializer = UpvoteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            post = Post.objects.get(pk=serializer.data["post"])
            post.upvotes += 1
            post.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
