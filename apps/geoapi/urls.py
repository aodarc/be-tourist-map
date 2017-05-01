from rest_framework.routers import DefaultRouter

from apps.geoapi.views import MarkerViewSet, SearchViewSet

router = DefaultRouter()
router.register(r'markers', MarkerViewSet)
router.register(r'search', SearchViewSet)
urlpatterns = router.urls
