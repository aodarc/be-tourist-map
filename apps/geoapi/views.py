from rest_framework import mixins
from rest_framework import viewsets

from apps.geoapi.serializers import MarkerSerializer
from apps.marker.models import Marker


class MarkerViewSet(mixins.CreateModelMixin,
                    mixins.ListModelMixin,
                    mixins.RetrieveModelMixin,
                    viewsets.GenericViewSet):
    queryset = Marker.objects.all()
    serializer_class = MarkerSerializer
