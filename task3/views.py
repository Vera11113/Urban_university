from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class Page(TemplateView):
    template_name = 'main_page.html'
