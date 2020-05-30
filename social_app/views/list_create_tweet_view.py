from django.db.models import Q
from rest_framework import generics,permissions
from rest_framework.response import Response

from ..models import Tweet, Like
from ..serializers import TweetSerializer
from ..permissions import IsOwnerOrReadOnly

class ListCreateTweetView(generics.ListCreateAPIView):
    queryset = Tweet.objects.all()
    serializer_class = TweetSerializer
    permissions = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user, type=0)

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        queryset = queryset.filter((Q(owner=request.user) | Q(is_public=True)) & Q(type=0))
        permission_class = [permissions.IsAuthenticatedOrReadOnly]
        for tweet in queryset:
            tweet_id = tweet.id
            likes_count = Like.objects.filter(tweet=tweet_id).count()

            tweet.likes_count = likes_count
            tweet.comments_count = tweet.comments.all().count()
            tweet.save()

        page = self.paginate_queryset(queryset)

        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
