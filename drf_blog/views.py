from rest_framework import generics, permissions
from rest_framework.exceptions import ValidationError
from .serializers import PostSerializer, VoteSerializer
from .models import Post, Vote


class PostList(generics.ListCreateAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(poster=self.request.user)
        
class VoteCreate(generics.CreateAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    serializer_class = VoteSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = user.request.user
        post = Post.objects.get(pk=self.kwargs['pk'])
        return Vote.objects.filter(voter=user, post=post)
        
    def perform_create(self, serializer):
        if self.get_queryset().exists():
            raise ValidationError('You have already voted for this post.')
        serializer.save(voter=self.request.user, post=Post.objects.get(pk=self.kwargs['pk']))
