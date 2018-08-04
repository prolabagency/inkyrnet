from django.urls import path
from .views import *

app_name = 'events'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('companies/', CompanyListView.as_view(), name='companies'),
    path('<int:pk>-<slug:slug>', EventDetailView.as_view()),
]
