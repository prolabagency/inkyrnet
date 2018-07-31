from django import forms
from redactor.widgets import RedactorEditor
from dal import autocomplete
from .models import Article


class ArticleAdminForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = '__all__'
        widgets = {
            'tags': autocomplete.TaggitSelect2('autocomplete'),
            'description': RedactorEditor()
        }