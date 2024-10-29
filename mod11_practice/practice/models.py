from django.db import models
from django.db.models import CharField, ForeignKey, DecimalField, IntegerField


# Create your models here.
class Category(models.Model):
    name = CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = CharField(max_length=100, unique=True)
    price = DecimalField(max_digits=10, decimal_places=2)
    stock = IntegerField(default=0)
    category = ForeignKey('Category', on_delete=models.CASCADE)

    def __str__(self):
        return self.name