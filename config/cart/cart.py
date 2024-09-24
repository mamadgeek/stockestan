from django.conf import settings
from products.models import Stock_laptops
class Cart(object): 

    def __init__(self,request): 
        ''''
        request.session # django request has session iself 
        settings.CART_SESSION_ID = 'cart' or...
        define the cart as a session which will be modified or ..

        '''
        self.session= request.session 
        cart= self.session.get(settings.CART_SESSION_ID)  # cart  
        if not cart:  
            # print('cart is none')  # cart is none 
            cart=self.session[settings.CART_SESSION_ID]= {}  #"eyJjYXJ0Ijp7fX0:1st2VS:pBhTcYXgIHANTFx5YqpqPkUgDP5Ac5XLX-9sH_Sgo7k"
                                                            # ".eJxVjDEOgzAMRe_iuYqSNjSEsXvPENmxXWgrkEiYEHdvkVhY_3vvr5BxrtCt2wUSLrVPS5E5DQwdODhthPkj4w74jeNrMnka6zyQ2RVz0GKeE8v3cbingx5L_69jtK4R9EG9KDokQevZBrJqiVqM1LC_BrUtZxHSGCm0wqji7oLxBtsPVcE8zw:1st2YP:Uq3xyYY5xBfgQ73PSYPlEPcfpUdUwphTMrB3G4I5ioA"
        self.cart=cart # local variable stored in instance variable 
    
    def add(self,laptop,laptop_count=1,update_count=False):
        '''
        get the id of laptop based our model
        and update it in 1 
        '''
        laptop_id= str(laptop.id) 
        if laptop_id not in self.cart: 
            self.cart[laptop_id] = {'laptop_count':0, # 0 due to adding in the bellow
                                    'price':str(laptop.price)}
        if update_count: 
            self.cart[laptop_id]['laptop_count'] = laptop_count
        else :
            self.cart[laptop_id]['laptop_count'] += laptop_count
        self.save()


    def show_cart(self):
        laptop_id= self.cart.keys()
        laptops= Stock_laptops.objects.filter(id__in= laptop_id)
        return laptops

    def save(self) :
        self.session[settings.CART_SESSION_ID] =self.cart
        self.session.moodified = True
        



        










