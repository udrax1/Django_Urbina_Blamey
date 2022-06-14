# Generated by Django 4.0.4 on 2022-05-28 20:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('idProducto', models.IntegerField(primary_key=True, serialize=False, verbose_name='Id del producto')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre del Producto')),
                ('precio', models.IntegerField(verbose_name='Precio')),
                ('stock', models.IntegerField(verbose_name='Stock')),
                ('image', models.ImageField(upload_to='productos')),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('idRegion', models.IntegerField(primary_key=True, serialize=False, verbose_name='Id region')),
                ('nombreRegion', models.CharField(max_length=50, verbose_name='Nombre Region')),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('rut', models.CharField(max_length=9, primary_key=True, serialize=False, verbose_name='Rut')),
                ('nombreCliente', models.CharField(max_length=50, verbose_name='Nombre cliente')),
                ('direccion', models.CharField(max_length=100, verbose_name='direccion')),
                ('image', models.ImageField(upload_to='clientes')),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='petfriends.region', verbose_name='Region')),
            ],
        ),
    ]
