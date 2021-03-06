from django.contrib.auth.models import User
from rest_framework import generics, permissions
from ..permissions import IsOwnerOrReadOnly
from ..serializers import UserSerializer


class UserDetailsView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]
