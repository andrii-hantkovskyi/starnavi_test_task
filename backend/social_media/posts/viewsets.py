from rest_framework.decorators import action
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, ListModelMixin
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST, HTTP_201_CREATED
from rest_framework.viewsets import GenericViewSet

from posts.models import Post
from posts.serializers import PostListRetrieveSerializer, PostCreateSerializer
from posts.services.common import like_post, dislike_post, create_post


class PostViewSet(GenericViewSet, CreateModelMixin, RetrieveModelMixin, ListModelMixin):
    queryset = Post.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_serializer_class(self):
        if self.action in ('list', 'retrieve'):
            return PostListRetrieveSerializer
        return PostCreateSerializer

    def create(self, request, *args, **kwargs):
        user = request.user
        data = request.data
        serializer = self.get_serializer(data=data)
        if not serializer.is_valid():
            return Response(status=HTTP_400_BAD_REQUEST)
        post = create_post(user, **serializer.validated_data)
        serialized_data = PostListRetrieveSerializer(post).data
        return Response(status=HTTP_201_CREATED, data=serialized_data)

    @action(methods=['POST'], detail=True, url_path='like')
    def like_post_req(self, request, pk=None):
        like_post(post_id=int(pk), user_id=request.user.id)
        return Response(status=HTTP_200_OK)

    @action(methods=['POST'], detail=True, url_path='dislike')
    def dislike_post_req(self, request, pk=None):
        dislike_post(post_id=pk, user_id=request.user.id)
        return Response(status=HTTP_200_OK)
