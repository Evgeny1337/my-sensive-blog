from django.contrib import admin
from blog.models import Post, Tag, Comment


class CommentsInline(admin.TabularInline):
    model = Comment
    extra = 0
    raw_id_fields = ('author',)
    verbose_name = 'Комментарий'
    verbose_name_plural = 'Комментарии'


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_at')
    inlines = [CommentsInline]
    raw_id_fields = ('author',)

    def get_queryset(self, request):
        return super().get_queryset(request).select_related('author')\
            .prefetch_related('comments')


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('title',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'post', 'published_at')
    raw_id_fields = ('post', 'author')
    search_fields = ('text',)
