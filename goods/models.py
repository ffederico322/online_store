from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=150, unique=True)
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True)

    class Meta:
        db_table = 'category'


class Product(models.Model):
    slug = models.SlugField()
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='goods_images', blank=True, null=True)
    quantity = models.PositiveIntegerField(default=0)
    price = models.DecimalField(default=0.00, max_digits=7, decimal_places=2, )
    discount = models.DecimalField(default=0.00, max_digits=7, decimal_places=2)
    promotion = models.BooleanField(default=False)

    category = models.ForeignKey(to=Category, on_delete=models.CASCADE)

    class Meta:
        db_table = 'product'


# class Users(models.Model):
#     username = models.CharField(max_length=255)
#     name = models.CharField(max_length=255)
#     surname = models.CharField(max_length=255)
#     avatar = models.FileField()
#
#
# class Carts(models.Model):
#     user = ''
#     product = ''
#     amount = models.IntegerField()
#     session_key = ''
#     creation_date = ''
#
#
# class Orders(models.Model):
#     user = ''
#     creation_date = ''
#     delivery_address = ''
#     payment_status = ''
#     delivery_status = ''
#
#
# class OrderedProduct(models.Model):
#     order = ''
#     product = ''
#     amount = models.IntegerField()
#     price = models.IntegerField()









