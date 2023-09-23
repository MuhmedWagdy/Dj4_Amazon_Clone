from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from utils.generate_code  import generate_code
from product.models import Product
import datetime

CART_STATUS = (
    ('Inprogress','Inprogress'),
    ('Completed','Completed'),
)

class Cart(models.Model):
    user =  models.ForeignKey(User,related_name='cart_user',on_delete=models.SET_NULL,null=True,blank=True)
    status = models.CharField( max_length=50,choices=CART_STATUS)

    def __str__(self):
        return str(self.user)
    
    def cart_total(self):
        total = 0 
        for item in self.cart_detail.all():
            total += item.total
        return total


class CartDetail(models.Model):
   cart = models.ForeignKey(Cart,related_name='cart_detail',on_delete=models.CASCADE)
   product = models.ForeignKey(Product,related_name='cart_product',on_delete=models.SET_NULL,null=True,blank=True)
   quantity = models.IntegerField()
   total = models.FloatField(null=True,blank=True)

   def __str__(self):
        return str(self.cart)
    
    
ORDER_STATUS = (
    ('Recieved','Recieved'),
    ('Processed','Processed'),
    ('Shipped','Shipped'),
    ('Delivered','Delivered'),
)

class Order(models.Model):
    user =  models.ForeignKey(User,related_name='order_user',on_delete=models.SET_NULL,null=True,blank=True)
    status = models.CharField( max_length=50,choices=ORDER_STATUS)
    code = models.CharField(max_length=100,default=generate_code())
    order_time = models.DateTimeField(default=timezone.now)
    delivery_time = models.DateTimeField(null=True,blank=True)
    coupon = models.ForeignKey('Coupon', related_name='order_coupon' ,on_delete=models.SET_NULL,null=True,blank=True)
    total_after_coupen= models.CharField(max_length=100,null=True,blank=True)

    def __str__(self):
        return str(self.user)


class OrderDetail(models.Model):
   order = models.ForeignKey(Order,related_name='order_detail',on_delete=models.CASCADE)
   product = models.ForeignKey(Product,related_name='order_product',on_delete=models.SET_NULL,null=True,blank=True)
   price = models.FloatField()
   quantity = models.IntegerField()
   total = models.FloatField(null=True,blank=True)

   def __str__(self):
        return str(self.order)


class Coupon(models.Model):
    code = models.CharField(max_length=100)
    discount = models.IntegerField()
    quantity = models.IntegerField()
    start_date = models.DateField(default=timezone.now)
    end_date = models.DateField(null=True,blank=True)
                                
   
    def __str__(self):
        return self.code
    

    def save(self, *args, **kwargs):
       week = datetime.timedelta(days=7)
       self.end_date = self.start_date + week       
       super(Coupon, self).save(*args, **kwargs) # Call the real save() method







