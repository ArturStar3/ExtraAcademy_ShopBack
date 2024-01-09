from .models import Product
from .serializers import ProductSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view()
def get_products(request):
    queryset = Product.objects.filter(quantity__gt=0, is_active=True)
    
    products = [ProductSerializer(query).data for query in queryset]

    return Response(products)


