from rest_framework import generics
from .serializers import PostSerializer
from .models import Post, Vote


class PostList(generics.ListAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer

