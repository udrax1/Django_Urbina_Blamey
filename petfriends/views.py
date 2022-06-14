from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators import csrf
from .models import Producto, Cliente, Region
from .forms import ProductoForm, ClienteForm
from django.contrib import messages
def index(request):
    return render(request, 'index.html')

def carrito(request):
    return render(request, 'carrito.html')

def galeria(request):
    return render(request, 'galeria.html')

def quienessomos(request):
    return render(request, 'quienessomos.html')

def registrarse(request):
    return render(request, 'registrarse.html')  

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
            return redirect('form_cliente')
    else:
        cliente_form= ClienteForm()
    return render(request, 'form_cliente.html', {'cliente_form': cliente_form})

def lista_clientes(request):
    clientes = Cliente.objects.all() 
    datosClientes = {
        'clientes': clientes 
    }
    return render (request, 'lista_clientes.html', datosClientes)

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

def eliminar_producto(request, id):
    producto= Producto.objects.get(idProducto=id)
    producto.delete()
    messages.success(request, "El Producto fue eliminado correctamente.")
    return redirect("lista_productos")

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

def eliminar_cliente(request, id):
    cliente= Cliente.objects.get(rut=id)
    cliente.delete()
    messages.success(request, "El Cliente fue eliminado correctamente.")
    return redirect("lista_clientes")

