from django.contrib.gis.geos import Point
from django.contrib.gis.measure import D
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
    def nearest(self, request):
        """
        Searching markers by coordinate near you
        :param request:
        :return:
        """
        serializer = PointSerializer(data=request.data)

        if serializer.is_valid():
            pnt = Point(serializer.unpack_data())
            radius = serializer.validated_data['distance']
            query = self.queryset.filter(position__distance_lte=(pnt, D(km=radius)))

            if len(query) < 3:
                query = self.queryset.filter(position__distance_lte=(pnt, D(km=radius+10)))

            return Response(
                {
                    "result": MarkerSerializer(query, many=True).data
                }, status=status.HTTP_200_OK)

        return Response(data={}, status=status.HTTP_200_OK)

    @list_route(methods=['post'])
    def all(self, request):
        pass
