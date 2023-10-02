from rest_framework.routers import SimpleRouter

from .viewsets import ExpenseViewSet, TransactionViewSet, DueViewSet, UserViewSet

urlpatterns = []

router = SimpleRouter()

router.register("user", UserViewSet, basename="user")
router.register("expense", ExpenseViewSet, basename="expense")
router.register("due", DueViewSet, basename="due")
router.register("transaction", TransactionViewSet, basename="transaction")

urlpatterns += router.urls

