# Generated by Django 4.0.4 on 2022-07-07 18:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('petfriends', '0009_alter_cliente_imagencli'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id_categoria', models.CharField(max_length=8, primary_key=True, serialize=False, verbose_name='Id categoria')),
                ('nombre', models.CharField(max_length=30, verbose_name='Categoria')),
            ],
        ),
        migrations.AddField(
            model_name='producto',
            name='id_categoria',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='petfriends.categoria', verbose_name='Categoria'),
        ),
    ]
