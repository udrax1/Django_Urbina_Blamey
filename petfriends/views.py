from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators import csrf
from .models import Producto, Cliente, Venta
from .forms import ProductoForm, ClienteForm, CustomUserCreationForm, ventaForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, permission_required
from django.views.decorators.http import require_POST
from .carrito import Carrito
from django.urls import reverse
from django.db.models import Q
import datetime

def index(request):
    return render(request, 'index.html')

def carrito(request):
    return render(request, 'carrito.html')

def tienda(request):
    productos = Producto.objects.all()
    return render(request, 'tienda.html', {'productos':productos} )



#lo de abajo carrito anterior  
def agregar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(idProducto=producto_id)
    carrito.agregar(producto)
    return redirect('carrito')
    

def eliminar_prod(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(idProducto=producto_id)
    carrito.eliminar(producto)
    return redirect('carrito')


def restar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(idProducto=producto_id)
    carrito.restar(producto)
    return redirect('carrito')

def limpiar_carrito(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect('tienda')

#lo de arriba carrito anterior 


def quienessomos(request):
    return render(request, 'quienessomos.html')


@permission_required('app.add_producto')
def form_producto(request):
    if request.method=='POST':
        producto_form = ProductoForm(request.POST ,request.FILES)
        if producto_form.is_valid():
            producto_form.save()
            messages.success(request, "Se ingreso el Producto correctamente.")
            return redirect('form_producto')
    else:
        producto_form= ProductoForm()
    return render(request, 'form_producto.html', {'producto_form': producto_form})

@permission_required('app.view_producto')
def lista_productos(request):
    productos = Producto.objects.all() #traigo todos los objetos de la clase Producto y los almaceno en 
    datosProductos = {
        'productos': productos  #diccionario para llamarlo desde el html
    }
    return render (request, 'lista_productos.html', datosProductos)


def form_cliente(request):
    if request.method=='POST':
        cliente_form = ClienteForm(request.POST ,request.FILES)
        if cliente_form.is_valid():
            cliente_form.save()
            messages.success(request, "Se ingreso el Cliente correctamente.")
            return redirect('index')
    else:
        cliente_form= ClienteForm()
    return render(request, 'form_cliente.html', {'cliente_form': cliente_form})

@permission_required('app.view_cliente')
def lista_clientes(request):
    clientes = Cliente.objects.all() 
    datosClientes = {
        'clientes': clientes 
    }
    return render (request, 'lista_clientes.html', datosClientes)

@permission_required('app.change_producto')
def mod_producto(request, id): 

    producto= Producto.objects.get(idProducto=id)
    datos={
        'form': ProductoForm(instance=producto)
    }
    if request.method=='POST':
        formulario=ProductoForm(data = request.POST, instance=producto, files=request.FILES)
        if formulario.is_valid():
            formulario.save() #lo sobreescribe
            messages.success(request, "El Producto fue modificado correctamente.")
            return redirect('lista_productos')
        
    return render(request, 'mod_producto.html', datos)

@permission_required('app.delete_producto')
def eliminar_producto(request, id):
    producto= Producto.objects.get(idProducto=id)
    producto.delete()
    messages.success(request, "El Producto fue eliminado correctamente.")
    return redirect("lista_productos")

@permission_required('app.change_cliente')
def mod_cliente(request, id):
    cliente= Cliente.objects.get(rut=id)
    datos={
        'form': ClienteForm(instance=cliente)
    }
    if request.method=='POST':
        formulario=ClienteForm(data = request.POST, instance=cliente, files=request.FILES)
        if formulario.is_valid():
            formulario.save() #lo sobreescribe
            messages.success(request, "El Cliente fue modificado correctamente.")
            return redirect('lista_clientes')
        
    return render(request, 'mod_cliente.html', datos)

@permission_required('app.delete_cliente')
def eliminar_cliente(request, id):
    cliente= Cliente.objects.get(rut=id)
    cliente.delete()
    messages.success(request, "El Cliente fue eliminado correctamente.")
    return redirect("lista_clientes")

def registro(request):
    data = {
        'form' : CustomUserCreationForm()
    }
    if request.method == 'POST':
        formulario= CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, user)
            messages.success(request, "Te haz registrado correctamente")
            return redirect(to="form_cliente")
        data["form"] = formulario
    return render(request, 'registration/registro.html', data)

def comprar(request):
    if request.method=='POST':
        venta_form = ventaForm(request.POST)
        if venta_form.is_valid():
            venta_form.save()
            messages.success(request, "Muchas gracias por tu compra <3")
            return redirect('index')
    else:
        venta_form= ventaForm()


    return render( request, 'comprar.html', {'venta_form': venta_form} )


def historial(request):
    queryset = request.GET.get("rut")
    venta = Venta.objects.filter(estado = True)
    if queryset:
        venta = Venta.objects.filter(
            Q(cliente_rut= queryset)
        )
    return render(request, 'historial.html', {'venta': venta})
