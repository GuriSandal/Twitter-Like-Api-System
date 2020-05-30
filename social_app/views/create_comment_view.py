from rest_framework import generics,permissions
from rest_framework.exceptions import NotFound

from ..models import Tweet, Comment
from ..serializers import CommentSerializer
from ..permissions import IsOwnerOrReadOnly

class CreateCommentView(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsOwnerOrReadOnly, permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        parent_id = int(self.request.data['parent'])
        tweets = Tweet.objects.filter(id=parent_id, is_public=True)

        if tweets.count() != 1:
            raise NotFound()

        serializer.save(owner=self.request.user, type=1, is_public=True, parent_id=parent_id)
