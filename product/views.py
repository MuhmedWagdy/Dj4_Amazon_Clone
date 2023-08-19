from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView,DetailView
from .models import Product,Brand,ProductImages,Review





class ProductList(ListView):

    model = Product


class ProductDetail(DetailView):
    model = Product

 

