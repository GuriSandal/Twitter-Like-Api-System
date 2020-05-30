from django.db.models import Q
from rest_framework import generics, permissions
from rest_framework.exceptions import NotFound

from ..models import Comment
from ..serializers import CommentSerializer
from ..permissions import IsOwnerOrReadOnly

class ListUpdateDeleteCommentView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    permissions = [permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]

    def perform_update(self, serializer):
        comment_id = int(self.kwargs.get('pk'))

        queryset = self.filter_queryset(self.queryset)
        queryset = queryset.filter(Q(id=comment_id) & Q(owner=self.request.user))

        if queryset.count() != 1:
            raise NotFound("Comment not found.")

        comment = queryset.get()

        serializer.save(parent=comment.parent, is_public=True)
