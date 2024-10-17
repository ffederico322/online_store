from django import template

from goods.models import Categories


register = template.Library()


@register.simple_tag()
def tag_categorties():
    return Categories.objects.all()