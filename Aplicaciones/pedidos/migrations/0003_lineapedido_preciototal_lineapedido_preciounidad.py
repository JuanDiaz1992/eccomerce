# Generated by Django 4.1.5 on 2023-01-12 00:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0002_alter_lineapedido_options_alter_pedido_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='lineapedido',
            name='PrecioTotal',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='lineapedido',
            name='precioUnidad',
            field=models.IntegerField(default=0),
        ),
    ]