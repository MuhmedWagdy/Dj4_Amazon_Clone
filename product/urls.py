from django.urls import path


from .views import ProductList,ProductDetail,BrandList,BrandDeatil

urlpatterns = [
    path('', ProductList.as_view()),
    path('<slug:slug>', ProductDetail.as_view()),
    path('brands/', BrandList.as_view()),
     path('brands/<slug:slug>', BrandDeatil.as_view()),

]