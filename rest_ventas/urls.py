from django.urls import path
from .views import lista_venta

urlpatterns =[
    path('lista_venta', lista_venta, name="lista_venta"),
]