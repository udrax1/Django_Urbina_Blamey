# Generated by Django 4.0.4 on 2022-07-13 02:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('petfriends', '0012_detalle_venta_cantidad_detalle_venta_precioproducto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estado_venta',
            name='estado',
            field=models.CharField(max_length=15, verbose_name='Estado'),
        ),
        migrations.DeleteModel(
            name='Detalle_Venta',
        ),
    ]
