from django import forms
from redactor.widgets import RedactorEditor
from .models import Job


class JobAdminForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = '__all__'
        widgets = {
            'description': RedactorEditor()
        }
