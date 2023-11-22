from django.shortcuts import render,redirect
from django.views.generic import ListView,DetailView
from .models import Product,Brand,ProductImages,Review
from django.db.models import Q , F
from django.db.models.aggregates import Min,Max,Sum,Count,Avg

from django.views.decorators.cache import cache_page

from .tasks import send_emails


from django.http import JsonResponse
from django.template.loader import render_to_string



@cache_page(60 * 1)
def queryset_debug(request):

    # data = Product.objects.select_related('brand').all()
    # data =  Product.objects.filter(price__gt= 20)
    # data =  Product.objects.filter(price__lte= 40)
    # data =  Product.objects.filter(price__range=(70,90))
    # data =  Product.objects.filter(brand___name='apple')
    # data =  Product.objects.filter(brand__price__gt=30)
    # data = Product.objects.filter(name__startswith='Kathy')
    # data = Product.objects.filter(name__endswith='Kathy')
    # data = Product.objects.filter(name__endswith='Mack')
    # data = Product.objects.filter(tags__isnull=True)
    # data = Review.objects.filter(created_at__year = 2023)
    # data = Product.objects.filter(price__gt=80 , quantity__lt=20)
    # data = Product.objects.filter(Q(price__gt=80) | Q(quantity__lt=20))
    # data = Product.objects.filter(~Q(price__gt=80) |Q(quantity__lt=20))
    # data = Product.objects.filter(price = F('quantity'))
    # data = Product.objects.all().order_by('name')
    # data = Product.objects.all().order_by('-name')
    # data = Product.objects.all()[10:40]
    # data = Product.objects.values('name','price','brand__name')
    # data = Product.objects.values('name','price')
   
    # data = Product.objects.defer('slug','discription')
    
    data = Product.objects.values_list('name','price')
    # data = Product.objects.aaggregate(Sum='quantaity')
    # data = Product.objects.aaggregate(Avg=Price)

    data = Product.objects.annotate(price_with_tax=F('price')*1.5)

    # data = Product.objects.get(id=30)
    send_emails.delay()




    # data = Product.objects.select_related('brand').all()
    # data = Product.objects.filter(
    #     Q(price__gt=80)|
    #     Q(quantity__gt=100)

    # )

    # data = Product.objects.filter(price=F('quantity'))
    return render(request,'product/debug.html',{'data':data})








class ProductList(ListView):

    model = Product
    paginate_by = 30


class ProductDetail(DetailView):
    model = Product
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["reviews"]= Review.objects.filter(product=self.get_object())
        context["related_products"] =  Product.objects.filter(brand=self.get_object().brand)
        return context

 

class BrandList(ListView):
    model = Brand

    queryset =  Brand.objects.annotate(product_count=Count('product_brand'))
    paginate_by = 20




class BrandDeatil(ListView):
    model = Product
    template_name = 'products/brand_detail.html'

    def get_queryset(self):
        brand = Brand.objects.get(slug=self.kwargs['slug'])
        return super().get_queryset().filter(brand=brand)
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["brand"] = Brand.objects.filter(slug=self.kwargs['slug']).annotate(product_count=Count('product_brand'))[0]
        return context
    
def add_review(request,slug):
    product = Product.objects.get(slug=slug)
    rate = request.POST['rate']
    review = request.POST['review']

    Review.objects.create(
        product = product ,
        rate = rate ,
        review = review ,
        user = request.user
    )

    reviews = Review.objects.filter(product=product)
    html = render_to_string('include/reviews_include.html',{'reviews':reviews})
    return JsonResponse({'result':html})
    # return redirect(f'/products/{product.slug}')


    
   







        
           
          

        




        
        




    
    