from django.contrib import admin

# Register your models here.


from .models import Product,ProductImages,Brand,Review


class ProductImagesTabular(admin.TabularInline):
    model = ProductImages



class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','flag','quantity','brand']
    list_filter = ['brand','flag']
    search_fields = ['name','subtitle','description']
    inlines = [ProductImagesTabular]


admin.site.register(Product,ProductAdmin)
admin.site.register(ProductImages)
admin.site.register(Brand)
admin.site.register(Review)
