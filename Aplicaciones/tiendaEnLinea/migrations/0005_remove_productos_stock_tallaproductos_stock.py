# Generated by Django 4.1.2 on 2023-02-23 03:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tiendaEnLinea', '0004_alter_productos_nombre'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productos',
            name='stock',
        ),
        migrations.AddField(
            model_name='tallaproductos',
            name='stock',
            field=models.IntegerField(default=1),
        ),
    ]