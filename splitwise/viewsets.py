from rest_framework import permissions
from rest_framework.mixins import (
    CreateModelMixin,
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
)
from rest_framework.viewsets import GenericViewSet

from .models import Expense, Transaction, Due
from .serializers import TransactionSerializer, ExpenseSerializer, DueSerializer


class ExpenseViewSet(GenericViewSet, RetrieveModelMixin, ListModelMixin, CreateModelMixin, UpdateModelMixin):
    permission_classes = [permissions.AllowAny]
    serializer_class = ExpenseSerializer
    queryset = Expense.objects.all()


class TransactionViewSet(GenericViewSet, CreateModelMixin, RetrieveModelMixin, ListModelMixin):
    permission_classes = [permissions.AllowAny]
    serializer_class = TransactionSerializer
    queryset = Transaction.objects.all()


class DueViewSet(GenericViewSet, ListModelMixin, RetrieveModelMixin):
    permission_classes = [permissions.AllowAny]
    serializer_class = DueSerializer
    queryset = Due.objects.all()


