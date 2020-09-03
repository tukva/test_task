from django.urls import include, path
from rest_framework import routers
from .views import PostViewSet, CommentViewSet, UpvoteList

router = routers.DefaultRouter()
router.register(r"posts", PostViewSet)
router.register(r"comments", CommentViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("upvotes/", UpvoteList.as_view()),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
]
