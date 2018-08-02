from django.urls import path
from magazine.views import *

urlpatterns = [
    path('', IndexView.as_view()),
    path('<int:pk>-<slug:slug>', ArticleDetailView.as_view()),
    path('companies/', CompanyListView.as_view()),
    path('<slug:slug>', CompanyDetailView.as_view()),
]
