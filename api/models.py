from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=225, unique=True)
    price = models.FloatField()
    description = models.TextField()
    quantity = models.IntegerField()
    category_id = models.IntegerField()
    is_active = models.BooleanField(default=True)
    
class Category(models.Model):
    name = models.CharField(max_length=225)