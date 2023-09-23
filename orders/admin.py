from django.contrib import admin

# Register your models here.

from .models import Cart,Cart_Detail,Order,Order_Detail,Coupon

admin.site.register(Cart)
admin.site.register(Cart_Detail)
admin.site.register(Order)
admin.site.register(Order_Detail)
admin.site.register(Coupon)

