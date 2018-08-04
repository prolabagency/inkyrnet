from django import forms
from redactor.widgets import RedactorEditor
from dal import autocomplete
from .models import Location, Event


class EventAdminForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = '__all__'
        widgets = {
            'tags': autocomplete.TaggitSelect2('autocomplete'),
            'description': RedactorEditor()
        }


class LocationAdminForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = '__all__'
        widgets = {
            'description': RedactorEditor()
        }
