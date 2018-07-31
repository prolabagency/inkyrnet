from dal import autocomplete
from taggit.models import Tag
from django.views.generic import TemplateView, ListView, DetailView
from magazine.models import Article


class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['latest_news'] = Article.objects.all().order_by('-id').filter(published=True)[0:4]
        return context


class TagAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated():
            return Tag.objects.none()
        qs = Tag.objects.all()
        if self.q:
            qs = qs.filter(name__istartswith=self.q)
        return qs
