from rest_framework.decorators import action
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, ListModelMixin
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST, HTTP_201_CREATED
from rest_framework.viewsets import GenericViewSet

from posts.models import Post
from posts.serializers import PostListRetrieveSerializer, PostCreateSerializer
from posts.services.common import like_post, dislike_post, create_post


class PostViewSet(GenericViewSet, CreateModelMixin, RetrieveModelMixin, ListModelMixin):
    queryset = Post.objects.all()

    def get_serializer_class(self):
        if self.action in ('list', 'retrieve'):
            return PostListRetrieveSerializer
        return PostCreateSerializer

    def create(self, request, *args, **kwargs):
        user = request.user
        title = request.data['title']
        body = request.data['body']
        post = create_post(user, title, body)
        serialized_data = PostListRetrieveSerializer(post).data
        return Response(status=HTTP_201_CREATED, data=serialized_data)

    @action(methods=['POST'], detail=True, url_path='like')
    def like_post_req(self, request, pk=None):
        try:
            like_post(post_id=int(pk), user_id=request.user.id)
            return Response(status=HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response(status=HTTP_400_BAD_REQUEST, data={'detail': str(e)})

    @action(methods=['POST'], detail=True, url_path='dislike')
    def dislike_post_req(self, request, pk=None):
        try:
            dislike_post(post_id=pk, user_id=request.user.id)
            return Response(status=HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response(status=HTTP_400_BAD_REQUEST, data={'detail': str(e)})
