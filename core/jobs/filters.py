from .models import Job
import django_filters
from jobs.models import TypeTime
from django import forms


class JobFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    type_time = django_filters.ModelMultipleChoiceFilter(queryset=TypeTime.objects.all(),
                                                         widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Job
        fields = ['title', 'type_time', 'technology', 'city']
