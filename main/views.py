from django.http import HttpResponse
from django.shortcuts import render

from goods.models import Categories

def index(request) -> HttpResponse:

    categories = Categories.objects.all()

    context: dict[str:str] = {
        'title': 'Federico - Главная',
        'content': 'Добро пожаловать в наш магазин!',
        'categories': categories
    }

    return render(request, 'main/index.html', context)


def about(request) -> HttpResponse:
    context: dict[str:str] = {
        'title': 'Federico - О нас',
        'content': 'Информация о магазине',
        'text': 'Текст...'
    }
    return render(request, 'main/about.html', context)



