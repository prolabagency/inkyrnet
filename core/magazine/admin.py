from django.contrib import admin
from .forms import ArticleAdminForm, CompanyAdminForm
from .models import Article, Company, Categories


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'likes', 'is_published', 'is_slide', 'author']
    list_filter = ['author']

    search_fields = ['title', 'description']
    prepopulated_fields = {"slug": ("title",)}
    readonly_fields = ['likes', 'edited_at', 'created_at', 'author', 'bookmark']
    form = ArticleAdminForm

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        obj.save()


class CompanyAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'email', 'likes', 'author']
    list_filter = ['author']

    search_fields = ['name', 'description']
    prepopulated_fields = {"slug": ("name",)}
    readonly_fields = ['likes', 'edited_at', 'created_at', 'author']
    form = CompanyAdminForm

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        obj.save()


class CategoriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        obj.save()


admin.site.register(Article, ArticleAdmin)
admin.site.register(Company, CompanyAdmin)
admin.site.register(Categories, CategoriesAdmin)
