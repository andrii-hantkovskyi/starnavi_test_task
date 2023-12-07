from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Post(models.Model):
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='posts', verbose_name='By user')
    title = models.CharField(max_length=255, verbose_name='Title')
    body = models.TextField(verbose_name='Post content')
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name='Created')
    last_updated = models.DateTimeField(
        auto_now=True, verbose_name='Last update')

    def __str__(self):
        return self.title


class PostLike(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='likes')
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='likes')
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name='Created')

    class Meta:
        verbose_name = 'Post like'
        verbose_name_plural = 'Post likes'

    def __str__(self):
        return f'Post {self.post.id}, by user {self.user.email}'
