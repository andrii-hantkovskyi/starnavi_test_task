from rest_framework.routers import DefaultRouter

from users.viewsets import UserViewSet

router = DefaultRouter()

router.register('', UserViewSet, basename='login')

urlpatterns = router.urls
