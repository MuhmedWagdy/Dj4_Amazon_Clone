from rest_framework import serializers

from .models import Product,Brand

class ProductSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class BrandSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'