from rest_framework import serializers

from .models import Product,Brand

class ProductSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class BrandListSerilizer(serializers.ModelSerializer):
    
    class Meta:
        model = Brand
        fields = '__all__'




class BrandDetailSerilizer(serializers.ModelSerializer):
    product = ProductSerilizer(source='product_brand',many=True)
    class Meta:
        model = Brand
        fields = '__all__'