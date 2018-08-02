from django import forms
from redactor.widgets import RedactorEditor
from dal import autocomplete
from .models import Article, Company


class ArticleAdminForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = '__all__'
        widgets = {
            'tags': autocomplete.TaggitSelect2('autocomplete'),
            'description': RedactorEditor()
        }


class CompanyAdminForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = '__all__'
        widgets = {
            'description': RedactorEditor()
        }
