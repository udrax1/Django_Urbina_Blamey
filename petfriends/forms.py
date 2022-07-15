from django import forms
from django.forms import ModelForm
from django.forms import widgets
from django.forms.models import ModelChoiceField
from django.forms.widgets import Widget
from .models import Producto, Cliente, Venta
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ProductoForm(forms.ModelForm):

    class Meta: 
        model= Producto
        fields = ['idProducto', 'nombre', 'precio', 'stock', 'imagenPro']
        labels ={
            'idProducto': 'Id Producto:', 
            'nombre': 'Nombre:', 
            'precio': 'Precio:', 
            'stock': 'Stock:',
            'imagenPro': 'Imagen:',
        }
        widgets={
            'idProducto': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese la id del producto', 
                    'id': 'idProducto'
                }
            ), 
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese su nombre', 
                    'id': 'nombre'
                }
            ), 
            'precio': forms.NumberInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese el precio', 
                    'id': 'precio'
                }
            ), 
            'stock': forms.NumberInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese el stock', 
                    'id': 'stock'
                }
            ),

            'imagenPro': forms.FileInput(
                attrs={
                    'class': 'file-input',
                    'id': 'imagenPro',
                    'style' : 'color: white ; background-color: green; text-align:center; width: 100%;'
                }
            )

        }

class ClienteForm(forms.ModelForm):

    class Meta: 
        model= Cliente
        fields = ['rut', 'nombreCliente', 'correo','telefono','direccion', 'region', 'imagenCli']
        labels ={
            'rut': 'Rut:', 
            'nombreCliente': 'Nombre Cliente:', 
            'correo': 'Email: ',
            'telefono': 'Teléfono',
            'direccion': 'Dirección:', 
            'region': 'Región:',
            'imagenCli': 'Imagen:',
        }
        widgets={
            'rut': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Sin puntos ni guion', 
                    'id': 'rut'
                }
            ), 
            'nombreCliente': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese su nombre', 
                    'id': 'nombreCliente'
                }
            ), 
            'correo': forms.EmailInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese su correo', 
                    'id': 'correo'
                }
            ) 
            ,
            'telefono': forms.NumberInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese su Telefono', 
                    'id': 'telefono'
                }
            )
            ,
            'direccion': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese su Dirección', 
                    'id': 'direccion'
                }
            ),
            'region': forms.Select(
                attrs={
                    'class': 'form-control',  
                    'id': 'region'
                }
            ),

            'imagenCli': forms.FileInput(
                attrs={
                    'class': 'file-input',
                    'id': 'imagenCli',
                    'style' : 'color: white ; background-color: green; text-align:center; width: 100%;'
                }
            )

        }

class ventaForm(forms.ModelForm):
    class Meta:
        model= Venta
        fields = ['id_venta', 'cliente_rut', 'total','fecha','estado']
        labels ={
            'id_venta': 'Id Venta:', 
            'cliente_rut': 'Rut:', 
            'total': 'total: ',
            'fecha': 'Fecha venta:',
            'estado': 'Estado de compra:', 
        }
        widgets={
            'id_venta': forms.TextInput(
            attrs={
                    'class': 'form-control', 
                    'placeholder': 'id venta', 
                    'id': 'id_venta'
            }
            ), 
            'cliente_rut': forms.TextInput(
            attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese su rut', 
                    'id': 'cliente_rut'
                }
            ), 
            'total': forms.NumberInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese el total', 
                    'id': 'total'
                }
            ) 
            ,
            'fecha': forms.DateInput(
                attrs={
                    'type': 'date',
                    'value': '2022-07-2022',
                    'class': 'form-control', 
                    'id': 'fecha'
                }
            )
            ,
            'estado': forms.Select(
                attrs={
                    'class': 'form-control',  
                    'id': 'estado'
                }
            )
        }

class CustomUserCreationForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email", "password1", "password2"]
        labels ={
            'username': 'username:', 
            'first_name': 'Nombre:', 
            'last_name': 'Apellidos: ',
            'email': 'Correo electronico:',
            'password1': 'Ingrese su contraseña:', 
            'password2': 'Repita su contraseña:',
        }

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]

class CartAddProductForm(forms.Form):
    cantidad = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES,
        coerce=int)
    actualizar = forms.BooleanField(required=False, initial=False,
                                widget=forms.HiddenInput)