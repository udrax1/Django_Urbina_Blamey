from django.urls import path
from .views import index, carrito, tienda, quienessomos, form_producto, \
    lista_productos, form_cliente, lista_clientes, mod_producto, eliminar_producto, \
    mod_cliente, eliminar_cliente, registro,agregar_producto, eliminar_prod, restar_producto, limpiar_carrito,\
    comprar, historial

    


urlpatterns = [
    path('', index, name="index"),#el primer html que mostrara
    path('carrito', carrito, name="carrito"),
    path('tienda', tienda, name="tienda"),
    path('quienessomos', quienessomos, name="quienessomos"),
    path('form_producto/', form_producto, name="form_producto"),
    path('lista_productos/', lista_productos, name="lista_productos"),
    path('form_cliente/', form_cliente, name="form_cliente"),
    path('lista_clientes/', lista_clientes, name="lista_clientes"),
    path('mod_producto/<id>', mod_producto, name="mod_producto"),
    path('eliminar_producto/<id>', eliminar_producto, name="eliminar_producto"),
    path('mod_cliente/<id>', mod_cliente, name="mod_cliente"),
    path('eliminar_cliente/<id>', eliminar_cliente, name="eliminar_cliente"),
    path('registro/', registro, name="registro"),
    path('agregar/<int:producto_id>/', agregar_producto, name="Add"),
    path('eliminar/<int:producto_id>/', eliminar_prod, name="Del"),
    path('restar/<int:producto_id>/', restar_producto, name="Sub"),
    path('limpiar/', limpiar_carrito, name="CLS"),
    path('comprar/', comprar, name="comprar"),
    path('historial/', historial, name="historial"),
    
    
]   