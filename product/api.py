from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ProductListSerilizer,ProductDetailSerilizer,BrandListSerilizer,BrandDetailSerilizer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from .mypagination import MyPagination
from rest_framework.permissions import IsAuthenticated
from .models import Product,Brand
from rest_framework import generics
from .myfilter import ProductFilter



@api_view(['GET'])
def product_list_api(request):                                 
    products = Product.objects.all()[:20]            
    data = ProductListSerilizer(products,many=True,context={'request':request}).data
    return Response({'products':data})

    # procuct = variable for all data 
    # data reterive data Serializer  

@api_view(['GET'])
def product_detail_api(request,product_id):
    products = Product.objects.get(id=product_id)
    data = ProductDetailSerilizer(products,context={'request':request}).data
    return Response({'products':data})
   
   #product  = product id return data 
   # context = path image to be urls for image reterive data image url    Function Based Views

class ProductListApi(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerilizer
    filter_backends = [DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter]
    filterset_fields = ['flag', 'brand','price']
    search_fields = ['name','subtitle','description']
    ordering_fields = ['price', 'quantity']
    filterset_class = ProductFilter
    pagination_class = MyPagination
    permission_classes = [IsAuthenticated]

   #class Based Views  use Generic ListCreatedAPIVIEW   WHEN CREATE CLASS NAME USE IP 


class ProductDetailApi(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerilizer


    #Class contain Queryset And Serilizer class from file serializer (QUERYSET == >  SERILIZER CLASS)


class BrandListApi(generics.ListAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandListSerilizer



class BrandDetailApi(generics.RetrieveAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandDetailSerilizer










