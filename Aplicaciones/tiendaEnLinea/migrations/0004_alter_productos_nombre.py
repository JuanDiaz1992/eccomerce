# Generated by Django 3.2.12 on 2023-01-27 04:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tiendaEnLinea', '0003_alter_imagenesproductos_colores'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productos',
            name='nombre',
            field=models.CharField(max_length=70),
        ),
    ]
