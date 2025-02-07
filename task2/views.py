from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
def func_url(request):
    title = 'new site'
    text = 'some text'
    context = {
        'title': title,
        'text': text
    }
    return render(request, 'func_template.html', context)

class Class_url(TemplateView):
    template_name = 'class_template.html'

