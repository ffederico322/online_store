from django.http import HttpResponse
from django.shortcuts import render


def catalog(request) -> HttpResponse:
    context: dict[str:str] = {
        'title': 'Federico - Главная',
         'content': 'Добро пожаловать в наш магазин!',
    }

    return render(request, 'goods/catalog.html', context)


def product(request) -> HttpResponse:
    context: dict[str:str] = {
        'title': 'Federico - О нас',
        'content': 'Информация о магазине',
        'text': 'Текст'
    }
    return render(request, 'goods/product.html', context)