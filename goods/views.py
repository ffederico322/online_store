from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from goods.models import Products


def catalog(request, category_slug) -> HttpResponse:

    if category_slug == 'all':
        goods = Products.objects.all()
    else:
        goods = get_object_or_404(Products.objects.filter(category__slug=category_slug))

    context: dict = {
        'title': 'Каталог',
        'goods': goods,
    }

    return render(request, 'goods/catalog.html', context)


def product(request, product_slug) -> HttpResponse:

    product = Products.objects.get(slug=product_slug)

    context = {
        'product': product
    }

    return render(request, 'goods/product.html', context=context)