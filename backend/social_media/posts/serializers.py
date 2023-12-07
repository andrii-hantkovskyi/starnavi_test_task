from rest_framework.serializers import ModelSerializer

from posts.models import Post, PostLike


class PostLikeSerializerMini(ModelSerializer):
    class Meta:
        model = PostLike
        fields = ('user',)


class PostListRetrieveSerializer(ModelSerializer):
    likes = PostLikeSerializerMini(many=True)

    class Meta:
        model = Post
        fields = ('id', 'title', 'body', 'created_at', 'created_by', 'likes')


class PostCreateSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = ('title', 'body')
