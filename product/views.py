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

 

