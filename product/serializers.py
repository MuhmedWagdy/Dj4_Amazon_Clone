from rest_framework import serializers

from .models import Product,Brand,Review

from django.db.models.aggregates import Avg

class BrandListSerilizer(serializers.ModelSerializer):
    
    class Meta:
        model = Brand
        fields = '__all__'





class ProductListSerilizer(serializers.ModelSerializer):
    brand = serializers.StringRelatedField()
    # brand = BrandListSerilizer()
    avg_rate = serializers.SerializerMethodField()
    reviews_count = serializers.SerializerMethodField()
    price_with_tax = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = '__all__'

    def get_price_with_tax(self,product):
        return product.price*1.5
    

    def get_avg_rate(self,product):
        avg = product.review_product.aggregate(rate_avg=Avg('rate'))
        if not avg['rate_avg']:
            result = 0
            return result
        return avg['rate_avg']
    

    def get_reviews_count(self,product:Product):
        reviews = product.review_product.all().count()
        return reviews

class ReviewsSerializer(serializers.ModelSerializer):
    class Meta:
        model= Review
        fields = '__all__'




class ProductDetailSerilizer(serializers.ModelSerializer):
    brand = serializers.StringRelatedField()
   
    avg_rate = serializers.SerializerMethodField()
    reviews_count = serializers.SerializerMethodField()
    reviews = ReviewsSerializer(source='review_product',many=True)

    class Meta:
        model = Product
        fields = '__all__'

    def get_avg_rate(self,product):
        avg = product.review_product.aggregate(rate_avg=Avg('rate'))
        if not avg['rate_avg']:
                result = 0
                return result
        return avg['rate_avg']
    

    def get_reviews_count(self,product:Product):
        reviews = product.review_product.all().count()
        return reviews






class BrandDetailSerilizer(serializers.ModelSerializer):
    product = ProductListSerilizer(source='product_brand',many=True)
    class Meta:
        model = Brand
        fields = '__all__'