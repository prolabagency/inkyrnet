from django import forms
from .models import Job


class JobAdminForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = '__all__'
        widgets = {
        }
