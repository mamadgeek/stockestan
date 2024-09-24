from django.contrib import admin
from .models import Stock_laptops
# Register your models here.

@admin.register(Stock_laptops)
class Stock_laptops_Admin(admin.ModelAdmin):
    pass


