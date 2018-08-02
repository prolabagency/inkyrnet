from dal import autocomplete
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from taggit.models import Tag
from django.views.generic import TemplateView, ListView, DetailView
from magazine.models import Article, Company


class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['latest_articles'] = Article.objects.all().order_by('-id').filter(published=True)[0:4]
        return context


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'magazine/article.html'

    def get_context_data(self, **kwargs):
        context = super(ArticleDetailView, self).get_context_data(**kwargs)
        context['article'] = Article.objects.get(pk=self.kwargs['pk'], published=True)
        return context


class CompanyListView(ListView):
    template_name = 'magazine/companies.html'
    model = Company
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super(CompanyListView, self).get_context_data(**kwargs)
        company_list = Company.objects.all().order_by('likes')
        paginator = Paginator(company_list, self.paginate_by)
        company = self.request.GET.get('company')
        try:
            file_company = paginator.page(company)
        except PageNotAnInteger:
            file_company = paginator.page(1)
        except EmptyPage:
            file_company = paginator.page(paginator.num_pages)
        context['companies'] = file_company
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
