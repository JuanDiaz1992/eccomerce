# Generated by Django 3.2.12 on 2023-03-06 23:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0002_lineapedido_stock'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lineapedido',
            name='stock',
        ),
    ]
