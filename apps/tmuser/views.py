from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework import viewsets
from rest_framework.decorators import detail_route, list_route
from rest_framework.response import Response

from apps.tmuser.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    User Endpoint view set
    """
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    user = get_user_model()

    @list_route(methods=['post'])
    def registration(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            user = serializer.create(serializer.validated_data)
            return Response(self.serializer_class(user).data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
