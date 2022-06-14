from django import forms
from django.forms import ModelForm
from django.forms import widgets
from django.forms.models import ModelChoiceField
from django.forms.widgets import Widget
from .models import Producto, Cliente, Region


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
        fields = ['rut', 'nombreCliente', 'direccion', 'region', 'imagenCli']
        labels ={
            'rut': 'Rut:', 
            'nombreCliente': 'Nombre Cliente:', 
            'direccion': 'Dirección:', 
            'region': 'Región:',
            'imagenCli': 'Imagen:',
        }
        widgets={
            'rut': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese el Rut', 
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
    
     

