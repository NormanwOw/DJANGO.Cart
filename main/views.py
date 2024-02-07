from django.shortcuts import render
from django.http.response import JsonResponse, Http404


def index(request):
    context = {
        'title': 'Главная',
        'counter': 1
    }
    return render(request, 'index.html', context)



