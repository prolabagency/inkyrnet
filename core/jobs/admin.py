from django.contrib import admin
from .forms import JobAdminForm
from .models import Job, Position, Technology, TypeTime


class JobAdmin(admin.ModelAdmin):
    list_display = ['title', 'technology', 'position', 'type_time', 'date_end']
    list_filter = ['technology', 'position', 'city']
    search_fields = ['title', 'description']
    prepopulated_fields = {"slug": ("title",)}
    readonly_fields = ['edited_at', 'created_at', 'author', 'bookmark']
    form = JobAdminForm

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        obj.save()


class PositionAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        obj.save()


class TechnologyAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        obj.save()


class TypeTimeAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        obj.save()


admin.site.register(Job, JobAdmin)
admin.site.register(Position, PositionAdmin)
admin.site.register(Technology, TechnologyAdmin)
admin.site.register(TypeTime, TypeTimeAdmin)
