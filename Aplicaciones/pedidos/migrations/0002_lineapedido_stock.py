# Generated by Django 3.2.12 on 2023-03-06 23:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tiendaEnLinea', '0005_alter_stock_unique_together'),
        ('pedidos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='lineapedido',
            name='stock',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='tiendaEnLinea.stock'),
            preserve_default=False,
        ),
    ]