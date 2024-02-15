from django.shortcuts import render
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

from carts.models import Product


def index(request):
    context = {
        'title': 'Главная',
        'counter': 1
    }
    return render(request, 'index.html', context)


class ProductsView(LoginRequiredMixin, ListView):
    template_name = 'products.html'
    queryset = Product.objects.all()
    context_object_name = 'products'
    extra_context = {'title': 'Товары'}



