from rest_framework import permissions
from rest_framework.mixins import RetrieveModelMixin, ListModelMixin, CreateModelMixin, UpdateModelMixin
from rest_framework.viewsets import GenericViewSet

from .models import User
from .serializers import UserSerializer


class UserViewSet(GenericViewSet, RetrieveModelMixin, ListModelMixin, CreateModelMixin, UpdateModelMixin):
    permission_classes = [permissions.AllowAny]
    serializer_class = UserSerializer
    queryset = User.objects.all()
