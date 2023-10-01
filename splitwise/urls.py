from rest_framework.routers import SimpleRouter

from splitwise.viewsets import ExpenseViewSet, TransactionViewSet, DueViewSet

urlpatterns = []

router = SimpleRouter()

router.register("expense", ExpenseViewSet, basename="expense")
router.register("due", DueViewSet, basename="due")
router.register("transaction", TransactionViewSet, basename="transaction")

urlpatterns += router.urls

