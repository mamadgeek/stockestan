from django.shortcuts import render , redirect, reverse ,get_object_or_404
from .cart import Cart
from products.models import Stock_laptops

def cart_add(request):
    cart = Cart(request)
    the_product=get_object_or_404(Stock_laptops,id=2)
    cart.add(the_product) 
    return redirect(reverse('cart:the_cart_detail'))


def cart_detail(request):
    cart= Cart(request)
    cart_items= cart.show_cart()
    return render (request , 'detail.html',{'cart_all': cart_items})


