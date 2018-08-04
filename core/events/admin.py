from django.contrib import admin
from .forms import EventAdminForm, LocationAdminForm
from .models import City, Location, Event


class EventAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_going', 'is_published', 'is_paid', 'author']
    list_filter = ['author', 'is_going', 'location']
    search_fields = ['title', 'description']
    prepopulated_fields = {"slug": ("title",)}
    readonly_fields = ['edited_at', 'created_at', 'author', 'bookmark', 'is_going']
    form = EventAdminForm

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        obj.save()


class LocationAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'site', 'city']
    list_filter = ['city']

    search_fields = ['name', 'description']
    prepopulated_fields = {"slug": ("name",)}
    form = LocationAdminForm

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        obj.save()


class CityAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        obj.save()


admin.site.register(Event, EventAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(City, CityAdmin)
