from django.shortcuts import render
from .models import Stock_laptops
from django.shortcuts import get_object_or_404 , render
from cart.cart import Cart

def index_page(request):
    Cart(request)  # this obj create a session of cart in this page
    limited_laptops=Stock_laptops.objects.all()[:5]
    return render (request,'index.html',context={'laptops':limited_laptops})

def laptop_page(request,pk):
    my_product= get_object_or_404(Stock_laptops,pk=pk)
    return render(request,'product.html',
                  context={'my_product':my_product}
                  )






