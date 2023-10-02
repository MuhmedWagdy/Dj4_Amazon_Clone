from rest_framework import generics
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from.serializers import CartSelializer,OrderDetailSerializer,OrderListSerializer
from .models import Cart , CartDetail,Order,OrderDetail,Coupon
from product.models import Product
import datetime


class CartDetailCreateAPI(generics.GenericAPIView):
    serializer_class = CartSelializer
    def get(self,request,*args,**kwargs):
        user =  User.objects.get(username=self.kwargs['username'])
        cart,created = Cart.objects.get_or_create(user=user,status='InProgress')
        data = CartSelializer(cart).data
        return Response({'cart':data})
    



    def post(self,request,*args,**kwargs):
         user =  User.objects.get(username=self.kwargs['username'])
         product = Product.objects.get(id=request.data['product_id'])
         quantity = int(request.data['quantity'])
         cart = Cart.objects.get(user=user,status= 'InProgress')
         cart_detail,created = CartDetail.objects.get_or_create(user=user,status='InProgress')
         cart_detail.quantity = quantity
         cart_detail.total = round(int(quantity)*product.price,2)
         cart_detail.save()

         cart = Cart.objects.get(user=user,status='InProgress')
         data = CartSelializer(cart).data
         return Response({'message':'Product delete successfullu','cart':data})
       



    def delete(self,request,*args,**kwargs):
          user =  User.objects.get(username=self.kwargs['username'])
          cart_detail = CartDetail.objects.get(id=request.data['cart_detail_id'])
          cart_detail.delete()
          cart = Cart.objects.get(user=user,status='inProgress')
          data = CartSelializer(cart).data
          return Response({'message':'product deleted Successfully','cart':data})
        





class OrderListAPI(generics.ListCreateAPIView):
     serializer_class = OrderListSerializer
     queryset = Order.objects.all()

     def list(self,request,*args,**wkargs):
          user = User.objects.get(username=self.kwargs['username'])
          queryset = self.get_queryset().filter(user=user)
          data = OrderListSerializer(queryset,many=True).data
          return Response(data)
     
    #  def get_queryset(self):
    #       queryset = super(OrderListAPI,self).get_queryset()
    #       user = User.objects.get(username=self.kwargs['username'])
    #       queryset = queryset.filter(user=user)
    #       return queryset



class OrderDetailAPI(generics.RetrieveAPIView):
     serializer_class = OrderListSerializer
     queryset = Order.objects.all()




class CreateOrderAPI(generics.GenericAPIView):
     def get(self,request,*args,**kwargs):
          user =  User.objects.get(username=self.kwargs['username'])
          cart = Cart.objects.get(user=user,status='InProgress')
          cart_detail = CartDetail.objects.filter(cart=cart)

          new_order = Order.objects.create(
               user = user,
               coupon = cart.coupon,
               total_after_coupon = cart.total_after_coupon
          )

          for object in cart_detail:
               OrderDetail.objects.create(
                    order = new_order ,
                    product = object.product ,
                    quantity = object.quantity,
                    price = object.product.price ,
                    total = round(int(object.quantity)*object.product.price,2)

                    )
               
          cart.status = 'Completed'
          cart.save()
          return Response({'message','Order Create Successfuly'})
               


       





class ApplyCouponAPI(generics.GenericAPIView):
     def post(self,request,*args,**kwargs):
          user = User.objects.get(username=self.kwargs['username'])
          cart = Cart.objects.get(user=user,status='InProgress')
          coupon =  get_object_or_404(Coupon,code=request.data['coupon_code'])

          if coupon and coupon.quantity > 0:
               today_date = datetime.datetime.today().date()

               if today_date >= coupon.start_date and today_date <= coupon.end_date:
                    coupon_value = Cart.cart_total() * coupon.discount/100
                    cart_total = cart.cart_total() - coupon_value
                    coupon.quantity -=1
                    coupon.save()
                    cart.coupon = coupon
                    cart.total_after_coupon = cart_total
                    cart.save()
                    cart = Cart.objects.get(user=user,status='InProgress')
                    data = CartSelializer(cart).data
                    return Response({'message':'coupon applied success','cart':data})
               else:
                    return Response({'message':'coupon date not found'})
          else:
               return Response ({'message','no coupon found'})
               



    



     
     
     