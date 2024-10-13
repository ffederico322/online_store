from django.db import models


class Categories(models.Model):
    name = models.CharField(max_length=150, unique=True)
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True)

    class Meta:
        db_table = 'categories'

    def __str__(self):
        return self.name



class Products(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='goods_images', blank=True, null=True)
    quantity = models.PositiveIntegerField(default=0)
    price = models.DecimalField(default=0.00, max_digits=7, decimal_places=2, )
    discount = models.DecimalField(default=0.00, max_digits=4, decimal_places=2)
    promotion = models.BooleanField(default=False)

    category = models.ForeignKey(to=Categories, on_delete=models.CASCADE)

    class Meta:
        db_table = 'products'

    def __str__(self):
        return self.name


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









