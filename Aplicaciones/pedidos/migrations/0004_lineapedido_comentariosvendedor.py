# Generated by Django 3.2.12 on 2023-03-07 01:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0003_remove_lineapedido_stock'),
    ]

    operations = [
        migrations.AddField(
            model_name='lineapedido',
            name='comentariosVendedor',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
