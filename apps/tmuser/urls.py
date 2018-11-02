from rest_framework.routers import DefaultRouter

from apps.tmuser.views import UserViewSet

app_name = 'tmuser'

router = DefaultRouter()
router.register(r'users', UserViewSet)
urlpatterns = router.urls
