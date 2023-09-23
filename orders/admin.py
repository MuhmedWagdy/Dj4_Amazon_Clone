from django.contrib import admin

# Register your models here.

from .models import Cart,CartDetail,Order,OrderDetail,Coupon

admin.site.register(Cart)
admin.site.register(CartDetail)
admin.site.register(Order)
admin.site.register(OrderDetail)
admin.site.register(Coupon)

