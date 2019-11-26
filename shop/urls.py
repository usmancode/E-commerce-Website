
from django.contrib import admin
from django.urls import path,include
from .import views

urlpatterns = [
    path('',views.index,name="ShopHome"),
    path('about/',views.about,name="about"),
    path('checkout/',views.checkout,name="Checkout"),
    path('contact/',views.contact,name="Contact Us"),
    path('products/<int:myid>',views.productView,name="ProductView"),
    path('search/',views.search,name="Search"),
    path('blog/',include('blog.urls')),
    path("handlerequest/", views.handlerequest, name="HandleRequest"),
   
]
