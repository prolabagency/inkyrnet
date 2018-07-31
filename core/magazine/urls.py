from django.urls import path
from magazine.views import *

urlpatterns = [
    path('', IndexView.as_view()),
    ]
