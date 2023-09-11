from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ProductSerilizer
from .models import Product

@api_view(['GET'])
def product_list_api(request):
    products = Product.objects.all()[:20]
    data = ProductSerilizer(products,many=True,context={'request':request}).data
    return Response({'products':data})



@api_view(['GET'])
def product_detail_api(request,product_id):
    products = Product.objects.get(id=product_id)
    data = ProductSerilizer(products,context={'request':request}).data
    return Response({'products':data})




