from django.shortcuts import render
from django.views.generic import ListView

from carts.models import Product


def index(request):
    context = {
        'title': 'Главная',
        'counter': 1
    }
    return render(request, 'index.html', context)


class ProductsView(ListView):
    template_name = 'products.html'
    queryset = Product.objects.all()
    context_object_name = 'products'



