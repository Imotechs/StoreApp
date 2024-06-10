
from django.urls import path
from . import views as inventoryViews

urlpatterns = [
    path('suppliers/', inventoryViews.Supplier_View),
    path('suppliers/<str:slug>/', inventoryViews.Supplier_View),
    path('items/',inventoryViews.InventoryItems_View),
    path('items/<str:slug>/',inventoryViews.InventoryItems_View),
]
