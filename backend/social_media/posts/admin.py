from django.contrib import admin

from posts.models import Post, PostLike

# Register your models here.

admin.site.register(Post)


@admin.register(PostLike)
class PostLikeAdmin(admin.ModelAdmin):
    fields = ('id', 'post', 'user', 'created_at')
    list_display = ('id', 'post', 'user', 'created_at')
    list_display_links = ('id',)
    list_filter = ('created_at', )
