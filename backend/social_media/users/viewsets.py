from django.contrib.auth import get_user_model
from rest_framework.mixins import CreateModelMixin
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from rest_framework.viewsets import GenericViewSet

from users.permissions import IsAuthenticatedOrCreateOnly
from users.serializers import UserSerializer, UserCreateSerializer
from users.services.auth import register_user

User = get_user_model()


class UserViewSet(GenericViewSet, CreateModelMixin):
    serializer_class = UserCreateSerializer
    queryset = User.objects.none()
    permission_classes = (IsAuthenticatedOrCreateOnly,)

    def create(self, request, *args, **kwargs):
        data = request.data
        serializer = self.get_serializer(data=data)

        if not serializer.is_valid():
            return Response(status=HTTP_400_BAD_REQUEST)

        user = register_user(**serializer.validated_data)
        serialized_data = UserSerializer(user).data

        return Response(status=HTTP_201_CREATED, data=serialized_data)
