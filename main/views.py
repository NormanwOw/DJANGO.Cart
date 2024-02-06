from django.shortcuts import render
from django.http.response import JsonResponse


def index(request):
    context = {
        'title': 'Главная',
        'counter': 0
    }
    return render(request, 'index.html', context)


counter = 0


def product_counter(request):
    global counter
    if request.method == 'POST':
        counter += 1
    data = {
        'counter': counter
    }
    return JsonResponse(data)
