from django.contrib.auth import get_user_model
from django.db import IntegrityError
from rest_framework.mixins import CreateModelMixin
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from rest_framework.viewsets import GenericViewSet

from users.permissions import IsAuthenticatedOrCreateOnly
from users.serializers import UserSerializer
from users.services.auth import register_user

User = get_user_model()


class UserViewSet(GenericViewSet, CreateModelMixin):
    serializer_class = UserSerializer
    queryset = User.objects.none()
    permission_classes = (IsAuthenticatedOrCreateOnly,)

    def create(self, request, *args, **kwargs):
        try:
            email = request.data.get('email')
            password = request.data.get('password')

            user = register_user(email, password)
            serialized_data = UserSerializer(user).data

            return Response(status=HTTP_201_CREATED, data=serialized_data)

        except IntegrityError as ex:
            return Response(status=HTTP_400_BAD_REQUEST)
