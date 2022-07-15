from django.contrib import admin
from .models import Producto, Cliente, Region, Estado_venta,Venta
# Register your models here.
admin.site.register(Estado_venta)
admin.site.register(Venta)
admin.site.register(Producto)
admin.site.register(Cliente)
admin.site.register(Region)