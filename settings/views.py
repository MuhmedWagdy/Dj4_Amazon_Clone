from django.shortcuts import render
from django.db.models import Count
from product.models import Product,Brand,Review

# from django.views.decorators.cache import cache_page



# @cache_page(60 * 60 * 24)
def home(request):
    brands = Brand.objects.all().annotate(product_count=Count('product_brand'))
    sale_products = Product.objects.filter(flag='Sale')[:10]
    featured_products = Product.objects.filter(flag='Feature')[:6]
    new_products =  Product.objects.filter(flag='New')[:10]
    reviews = Review.objects.all()[:5]

   
    

    return render(request,'settings/home.html',{
        'brands':brands,
        'sale_products':sale_products,
        'featured_products':featured_products,
        'new_products':new_products,
        'reviews':reviews
    })
   



