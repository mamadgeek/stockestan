from django.urls import path
from .views import cart_add , cart_detail
app_name='cart'

urlpatterns= [
    path('detail/',cart_detail,name='the_cart_detail'),
    path('add/',cart_add,name='the_cart_adding')
]










