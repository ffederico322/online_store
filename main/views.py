from django.http import HttpResponse
from django.shortcuts import render


def index(request) -> HttpResponse:
    return render(request, 'main/index.html')


def about(request) -> HttpResponse:
    return render(request, 'main/about.html')



