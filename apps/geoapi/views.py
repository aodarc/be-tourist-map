from django.contrib.gis.geos import Point
from rest_framework import mixins
from rest_framework import status
from rest_framework import viewsets
from rest_framework.decorators import list_route
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response

from apps.geoapi.serializers import MarkerSerializer, PointSerializer
from apps.marker.models import Marker


class MarkerViewSet(mixins.CreateModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.ListModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.DestroyModelMixin,
                    viewsets.GenericViewSet):
    queryset = Marker.objects.all()
    serializer_class = MarkerSerializer
    # parser_classes = (FileUploadParser, )

    # def put(self, request, filename, format=None):
    #     file_obj = request.FILES['file']
    #     # do some stuff with uploaded file
    #     return Response(status=204)


class SearchViewSet(viewsets.ViewSet):
    queryset = Marker.objects.all()
    serializer_class = MarkerSerializer

    @list_route(methods=['post'])
    def by_coordinates(self, request):
        serializer = PointSerializer(data=request.data)

        if serializer.is_valid():
            pnt = Point(serializer.unpack_data())


        return Response(data={}, status=status.HTTP_200_OK)

    @list_route(methods=['post'])
    def nearest(self, request):
        pass
