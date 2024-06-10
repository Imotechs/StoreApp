from django.contrib import admin

# Register your models here.
from .models import Supplier,InventoryItem

admin.site.register(Supplier)
admin.site.register(InventoryItem)