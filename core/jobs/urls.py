from django.urls import path
from .views import *
from django_filters.views import FilterView

app_name = 'jobs'

urlpatterns = [
    path('', FilterView.as_view(filterset_class=JobFilter,
                                template_name='jobs/job_list.html'), name='index'),
    path('companies/', CompanyListView.as_view(), name='companies'),
]
