from rest_framework import generics,permissions

from ..models import Tweet
from ..serializers import TweetSerializer
from ..permissions import IsOwnerOrReadOnly

class ListUpdateDeleteTweetView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tweet.objects.all()
    serializer_class = TweetSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]
    
