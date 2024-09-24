
from .views import index_page , laptop_page
from django.contrib import admin
from django.urls import path , include

urlpatterns = [
    path('',index_page,name='index_page'),
    path('laptop/<int:pk>/',laptop_page,name='laptop_page'),
    path('cart/',include('cart.urls')),
]

