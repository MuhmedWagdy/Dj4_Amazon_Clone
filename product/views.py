from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView,DetailView
from .models import Product,Brand,ProductImages,Review





class ProductList(ListView):

    model = Product


class ProductDetail(DetailView):
    model = Product
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["reviews"]= Review.objects.filter(product=self.get_object())
        context["related_products"] =  Product.objects.filter(brand=self.get_object().brand)
        return context

 

class BrandList(ListView):
    model = Brand


class BrandDeatil(ListView):
    model = Product

    template_name = 'products/brand_detail.html'

    def get_queryset(self):
        brand = Brand.objects.get(slug=self.kwargs['slug'])
        return super().get_queryset().filter(brand=brand)
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["brand"] = Brand.objects.get(slug=self.kwargs['slug'])
        return context
    
    




