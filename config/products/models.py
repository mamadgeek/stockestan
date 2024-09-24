
from django.db import models 
from django.urls import reverse


class Stock_laptops(models.Model):
    id=models.AutoField(primary_key=True)
    brand_choices=(('dell','Dell'),('lenovo','Lenovo'),('asus','Asus'),('aser','Aser'),('Fojisto','fojisto'),('macbook','Apple Macbook'),('microsoft','Microsoft'))
    model_name= models.CharField(max_length=320,null=True,blank=True)
    brand= models.CharField(max_length=220,choices=brand_choices,null=True,blank=True)
    ussing_status= models.CharField(max_length=220,choices=(('used','کارکرده'),('new','تازه'),('stock','استوک')))
    price= models.DecimalField(max_digits=20,decimal_places=3,null=True,blank=True)
    offer= models.PositiveIntegerField( null=True,blank=True)
    created_at= models.DateTimeField(auto_now_add=True,)
    updated_at= models.DateTimeField(auto_now=True,)
    # created_by= models.DateTimeField(user,null=True,blank=True)
    cpu_model= models.CharField(max_length=220)
    ram_model= models.CharField(max_length=220)
    graphic_model=models.CharField(max_length=220)
    hard_model=models.CharField(max_length=220)
    monitor_model=models.CharField(max_length=220)
    body_issues= models.CharField(max_length=220,null=True,default=None)
    images=models.ImageField()
    weak_points= models.CharField(max_length=220)
    images=  models.ImageField(upload_to='stock_laptop/%Y/%m/%d',blank=True)
    # price_in_another_sites
    # comments=  
    class Meta: 
        ordering=('-created_at',)

    def __str__(self) -> str:
        return f"{self.model_name} - {self.brand}"
    # def __str__(self) -> str:
    #     return f"{self.id}"
    
    def get_absolute_url(self):
        return reverse('laptop_page', kwargs={'pk': self.id})
    
