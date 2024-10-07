from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)


class Product(models.Model):
    slug = models.SlugField()
    name = models.CharField()
    description = models.CharField()
    image = models.FileField()
    amount = models.IntegerField()
    price = models.IntegerField()
    discount = models.IntegerField()
    promotion = models.BooleanField(default=False)

    category = Category.pk


class Users(models.Model):
    username = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    avatar = models.FileField()


class Carts(models.Model):
    user = ''
    product = ''
    amount = models.IntegerField()
    session_key = ''
    creation_date = ''


class Orders(models.Model):
    user = ''
    creation_date = ''
    delivery_address = ''
    payment_status = ''
    delivery_status = ''


class OrderedProduct(models.Model):
    order = ''
    product = ''
    amount = models.IntegerField()
    price = models.IntegerField()









