from django.conf.urls.static import static
from core import settings
from django.contrib import admin
from django.conf.urls import url
from django.urls import path, include
from magazine.views import TagAutocomplete
from jobs.views import SalariesView
from magazine.views import CompanyDetailView
from events.views import CompanyEventDetailView
from jobs.views import CompanyJobDetailView, JobDetailView

urlpatterns = [
    path('', include('magazine.urls')),
    path('admin/', admin.site.urls),
    path('redactor/', include('redactor.urls')),
    path('events/', include('events.urls')),
    path('jobs/', include('jobs.urls')),
    path('salaries/', SalariesView.as_view(), name='salaries'),
    path('edu/', include('edu.urls')),
    path('<slug:slug>/', CompanyDetailView.as_view(), name='company_articles'),
    path('<slug:slug>/events/', CompanyEventDetailView.as_view(), name='company_events'),
    path('<slug:slug>/jobs/', CompanyJobDetailView.as_view(), name='company_jobs'),
    path('job/<int:pk>-<slug:slug>', JobDetailView.as_view()),
    url(r'autocomplete/$', TagAutocomplete.as_view(), name='autocomplete'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
