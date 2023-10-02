from rest_framework import permissions
from rest_framework.decorators import action
from rest_framework.mixins import (
    CreateModelMixin,
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin, DestroyModelMixin,
)
from rest_framework.viewsets import GenericViewSet

from .models import Expense, Transaction, Due, User
from .serializers import TransactionSerializer, ExpenseSerializer, DueSerializer, UserSerializer


class UserViewSet(GenericViewSet, RetrieveModelMixin, ListModelMixin, CreateModelMixin, UpdateModelMixin):
    permission_classes = [permissions.AllowAny]
    serializer_class = UserSerializer
    queryset = User.objects.all()


class ExpenseViewSet(GenericViewSet, RetrieveModelMixin, ListModelMixin, CreateModelMixin, UpdateModelMixin):
    permission_classes = [permissions.AllowAny]
    serializer_class = ExpenseSerializer
    queryset = Expense.objects.all()


class TransactionViewSet(GenericViewSet, RetrieveModelMixin, ListModelMixin):
    permission_classes = [permissions.AllowAny]
    serializer_class = TransactionSerializer
    queryset = Transaction.objects.all()


class DueViewSet(GenericViewSet, ListModelMixin, RetrieveModelMixin, DestroyModelMixin):
    permission_classes = [permissions.AllowAny]
    serializer_class = DueSerializer
    queryset = Due.objects.all()

    @action(
        methods=["DELETE"],
        detail=True
    )
    def settle(self, request, *args, **kwargs):
        instance = self.get_object()
        Transaction.objects.create(
            from_user=instance.from_user,
            to_user=instance.from_user,
            amount=instance.amount,
            contribution=instance.contribution
        )
        self.perform_destroy(instance)

