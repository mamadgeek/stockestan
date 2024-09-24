from django.db import models
from users.models import Custumers ,Admins
from products.models import Stock_laptops

class Order(models.Model):
    custumer=models.ForeignKey(Custumers,on_delete=models.CASCADE)
    order_date=models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.id}"
    
    

class OrderItem(models.Model):
    id= models.AutoField(primary_key=True)
    order= models.ForeignKey(Order,on_delete=models.CASCADE)
    product= models.ForeignKey(Stock_laptops,on_delete=models.CASCADE)
    product_price=models.DecimalField(max_digits=20,decimal_places=3)
    count= models.PositiveIntegerField(default=1)
    total_price= models.DecimalField(max_digits=20,decimal_places=3)

    def __str__(self) -> str:
        return f"{self.product}"

class Invoice(models.Model):
    id=models.AutoField(primary_key=True)
    #  this must be considered 
    order=models.ForeignKey(OrderItem,on_delete=models.CASCADE)
    order_date= models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return f"{self.id}"

class Transaction(models.Model):
    id=models.AutoField(primary_key=True)
    STATUS_CHOICES=(('pending','Pending'),('paid','Paid'),('canceled','Canceled'))
    status=models.CharField(max_length=220,choices=STATUS_CHOICES,default='pending')
    # paid_methode= 
    invoice=models.ForeignKey(Invoice,on_delete=models.CASCADE)
    transaction_date=models.DateTimeField(auto_now_add=True)
    amount = models.DecimalField(max_digits=20,decimal_places=3)

    def __str__(self) -> str:
        return f"{self.id}"



