from django.conf.urls.static import static
from core import settings
from django.contrib import admin
from django.conf.urls import url
from django.urls import path, include
from magazine.views import TagAutocomplete

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^redactor/', include('redactor.urls')),
    url(r'^autocomplete/$', TagAutocomplete.as_view(), name='autocomplete'),
    path('', include('magazine.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)