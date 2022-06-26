from distutils.command.upload import upload
from django.db import models
from tkinter import CASCADE
from tkinter.tix import Tree



# Create your models here.
class Producto(models.Model):
    idProducto = models.IntegerField(primary_key=True, verbose_name='Id del producto')
    nombre= models.CharField(max_length=50, verbose_name='Nombre del Producto')
    precio= models.IntegerField( verbose_name='Precio')
    stock= models.IntegerField(verbose_name='Stock')
    imagenPro= models.ImageField(upload_to="productos")

    def __str__(self):
        return self.nombre

class Region(models.Model):
    idRegion= models.IntegerField(primary_key=True, verbose_name='Id region')
    nombreRegion = models.CharField(max_length=50, verbose_name='Nombre Region')

    def __str__(self):
        return self.nombreRegion

class Cliente(models.Model):
    rut= models.CharField(primary_key=True, max_length=9, verbose_name='Rut')
    nombreCliente= models.CharField(max_length=50, verbose_name='Nombre cliente')
    correo= models.EmailField(verbose_name='E-mail', null=True)
    telefono= models.IntegerField(verbose_name='teléfono:', null=True)
    direccion= models.CharField(max_length=100, verbose_name='Direccion')
    region= models.ForeignKey(Region, on_delete=models.CASCADE, verbose_name='Region')
    imagenCli= models.ImageField(upload_to="clientes")

    def __str__(self):
        return self.rut