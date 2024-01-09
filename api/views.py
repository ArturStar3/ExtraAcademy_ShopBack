from django.shortcuts import render
from django.http import JsonResponse
from .models import Product
import json

def get_products(request):
    products = Product.objects.filter(quantity__gt=0, is_active=True)
    products_dict={}
    for product in products:
        products_dict[product.name]={
            'price': product.price,
            'description': product.description,
            'quantity': product.quantity,
            'category_id': product.category_id,
        }
    return JsonResponse(products_dict)


