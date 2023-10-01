from rest_framework.routers import SimpleRouter

from .viewsets import UserViewSet

urlpatterns = []

router = SimpleRouter()

router.register("user", UserViewSet, basename="user")

urlpatterns += router.urls
