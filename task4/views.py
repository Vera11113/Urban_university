from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
def shop(request):
    context = {
        'games': ['Atomic Heart', 'Cyberpunk2077']
    }
    return render(request, 'shop_page.html', context)

def main_func(request):
    return render(request, 'main_page.html')

def cart(request):
    return render(request, 'cart_page.html')
