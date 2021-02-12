from rest_framework.viewsets import ModelViewSet
from .serializer import UserSerializer
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            User.objects.create_user(
                **request.data
            )
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, *args, **kwargs):
        return Response({'message': 'METHOD GET IS NOT ALLOWED'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def list(self, request, *args, **kwargs):
        return Response({'message': 'METHOD GET IS NOT ALLOWED'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)