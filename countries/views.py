# Django
from django.shortcuts import render
from django.views.generic import ListView

# Models
from countries.models import Country

class CountriesFeedView(ListView):
    template_name = 'countries/feed.html'
    model = Country
    paginate_by = 10
    context_object_name = 'countries'