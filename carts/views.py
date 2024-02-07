from django.http import Http404, JsonResponse
from django.shortcuts import render


def cart(request):
    return render(request, 'cart.html', {'title': 'Корзина'})


def new_order(request):
    if request.method == 'POST':
        data = request.POST
        return JsonResponse(data)

    raise Http404
