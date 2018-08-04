from dal import autocomplete
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from taggit.models import Tag
from django.db.models import Count
from django.views.generic import TemplateView, ListView, DetailView
from magazine.models import Article, Company


class IndexView(TemplateView):
    template_name = "magazine/index.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['articles'] = Article.objects.all().order_by('-id').filter(is_published=True)
        return context


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'magazine/article.html'

    def get_context_data(self, **kwargs):
        context = super(ArticleDetailView, self).get_context_data(**kwargs)
        context['article'] = Article.objects.get(pk=self.kwargs['pk'], is_published=True)
        return context


class CompanyListView(ListView):
    template_name = 'magazine/companies.html'
    model = Article
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super(CompanyListView, self).get_context_data(**kwargs)
        company_list = Company.objects.annotate(num_articles=Count('company_articles')).order_by('-num_articles')
        context['article_companies'] = company_list
        return context


class CompanyDetailView(DetailView):
    model = Company
    template_name = 'magazine/company.html'

    def get_context_data(self, **kwargs):
        context = super(CompanyDetailView, self).get_context_data(**kwargs)
        context['company'] = Company.objects.get(slug=self.kwargs['slug'])
        context['articles'] = Article.objects.filter(company__slug=self.kwargs['slug'])
        return context


class TagAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated():
            return Tag.objects.none()
        qs = Tag.objects.all()
        if self.q:
            qs = qs.filter(name__istartswith=self.q)
        return qs
