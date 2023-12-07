from django.contrib.auth.models import User

from posts.models import PostLike, Post


def create_post(user: User, title: str, body: str) -> Post:
    return Post.objects.create(created_by=user, title=title, body=body)


def like_post(post_id: int, user_id: int) -> None:
    PostLike.objects.create(post_id=post_id, user_id=user_id)


def dislike_post(post_id: int, user_id: int) -> None:
    postlike = PostLike.objects.get(post_id=post_id, user_id=user_id)
    postlike.delete()
