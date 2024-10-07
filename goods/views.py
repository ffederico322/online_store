from django.http import HttpResponse
from django.shortcuts import render


def catalog(request) -> HttpResponse:
    context: dict = {
        'title': 'Каталог',
        'goods': [
            {
        'name': 'Название товара',
        'description': 'Описание',
        'image': '',
        'price': 150
    }
        ],
    }

    return render(request, 'goods/catalog.html', context)


def product(request) -> HttpResponse:
    context: dict = {
        'title': 'название товара'
    }
    return render(request, 'goods/product.html', context)