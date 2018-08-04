from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.views.generic import TemplateView, ListView, DetailView
from .models import Job
from django.contrib.auth.models import User
from django.shortcuts import render
from .filters import JobFilter
from django.db.models import Count
from magazine.models import Company


class IndexView(TemplateView):
    template_name = "jobs/index.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['jobs'] = Job.objects.all().order_by('date_end')
        return context


class JobDetailView(DetailView):
    model = Job
    template_name = 'jobs/job.html'

    def get_context_data(self, **kwargs):
        context = super(JobDetailView, self).get_context_data(**kwargs)
        context['job'] = Job.objects.get(slug=self.kwargs['slug'])
        return context


class CompanyListView(ListView):
    template_name = 'jobs/companies.html'
    model = Job
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super(CompanyListView, self).get_context_data(**kwargs)
        company_list = Company.objects.annotate(num_articles=Count('job_company')).order_by('-num_articles')
        context['job_companies'] = company_list
        return context


class CompanyJobDetailView(DetailView):
    model = Company
    template_name = 'jobs/company.html'

    def get_context_data(self, **kwargs):
        context = super(CompanyJobDetailView, self).get_context_data(**kwargs)
        context['company'] = Company.objects.get(slug=self.kwargs['slug'])
        context['jobs'] = Job.objects.filter(company__slug=self.kwargs['slug'])
        return context


class SalariesView(TemplateView):
    template_name = "jobs/salaries.html"

    def get_context_data(self, **kwargs):
        context = super(SalariesView, self).get_context_data(**kwargs)
        return context


def search(request):
    user_list = Job.objects.all()
    user_filter = JobFilter(request.GET, queryset=user_list)
    return render(request, 'jobs/job_list.html', {'filter': user_filter})

