from django.contrib import admin
from .forms import ArticleAdminForm
from .models import Article


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'likes', 'published', 'slide', 'author']
    list_filter = ['author']

    search_fields = ['title', 'description']
    prepopulated_fields = {"slug": ("title",)}
    readonly_fields = ['likes', 'edited_at', 'created_at', 'author', 'bookmark']
    form = ArticleAdminForm

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        obj.save()


admin.site.register(Article, ArticleAdmin)