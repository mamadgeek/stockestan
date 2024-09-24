from django.contrib import admin
from .models import Custumers , Admins
# Register your models here.

@admin.register(Custumers)
class CustumersAdmin(admin.ModelAdmin):
    pass

@admin.register(Admins)
class AdminsAdmin(admin.ModelAdmin):
    pass