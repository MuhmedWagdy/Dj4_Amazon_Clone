from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ProductListSerilizer,ProductDetailSerilizer,BrandListSerilizer,BrandDetailSerilizer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from .models import Product,Brand
from rest_framework import generics

from .myfilter import ProductFilter



@api_view(['GET'])
def product_list_api(request):
    products = Product.objects.all()[:20]
    data = ProductListSerilizer(products,many=True,context={'request':request}).data
    return Response({'products':data})



@api_view(['GET'])
def product_detail_api(request,product_id):
    products = Product.objects.get(id=product_id)
    data = ProductDetailSerilizer(products,context={'request':request}).data
    return Response({'products':data})


class ProductListApi(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerilizer
    filter_backends = [DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter]
    filterset_fields = ['flag', 'brand','price']
    search_fields = ['name','subtitle','description']
    ordering_fields = ['price', 'quantity']
    filterset_class = ProductFilter




class ProductDetailApi(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerilizer



class BrandListApi(generics.ListAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandListSerilizer


class BrandDetailApi(generics.RetrieveAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandDetailSerilizer













