from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.views.generic import TemplateView, ListView, DetailView
from .models import Event
from django.db.models import Count
from magazine.models import Company


class IndexView(TemplateView):
    template_name = "event/index.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['events'] = Event.objects.all().order_by('-id').filter(is_published=True)
        return context


class EventDetailView(DetailView):
    model = Event
    template_name = 'event/event.html'

    def get_context_data(self, **kwargs):
        context = super(EventDetailView, self).get_context_data(**kwargs)
        context['event'] = Event.objects.get(pk=self.kwargs['pk'], is_published=True)
        return context


class CompanyListView(ListView):
    template_name = 'event/companies.html'
    model = Event
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super(CompanyListView, self).get_context_data(**kwargs)
        company_list = Company.objects.annotate(num_articles=Count('event_company')).order_by('-num_articles')
        context['event_companies'] = company_list
        return context


class CompanyEventDetailView(DetailView):
    model = Company
    template_name = 'event/company.html'

    def get_context_data(self, **kwargs):
        context = super(CompanyEventDetailView, self).get_context_data(**kwargs)
        context['company'] = Company.objects.get(slug=self.kwargs['slug'])
        context['events'] = Event.objects.filter(company__slug=self.kwargs['slug'])
        return context
