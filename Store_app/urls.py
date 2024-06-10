
from django.contrib import admin
from django.urls import path,include
from inventory.views import endpoint

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',endpoint, name ='endpoints'),
    path('api/',include('inventory.urls')),
]
