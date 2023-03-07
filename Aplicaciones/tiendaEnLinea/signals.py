# archivo signals.py
from django.db.models.signals import post_save,pre_delete,pre_save
from django.dispatch import receiver
from .models import Stock,Categoria,Productos
from django.db.models import Sum
import os
from decimal import Decimal

from Aplicaciones.pedidos.models import Pedido, LineaPedido




@receiver(post_save, sender=Stock)
def actualizar_stock_total(sender, instance, **kwargs):
    producto = instance.producto
    stock_total_dict = Stock.objects.filter(producto=producto).aggregate(sum_stock=Sum('stock'))
    stock_total = stock_total_dict['sum_stock'] if stock_total_dict['sum_stock'] is not None else 0
    producto.stock_total = stock_total
    producto.save()
def eliminar_imagen_stock(sender, instance, **kwargs):
    # Eliminar la imagen correspondiente si existe
    if instance.imagen:
        os.remove(instance.imagen.path)



@receiver(pre_delete, sender=Categoria)
def eliminar_imagen_categoria(sender, instance, **kwargs):
    # Eliminar la imagen correspondiente si existe
    if instance.imagen:
        os.remove(instance.imagen.path)



@receiver(pre_save, sender=Productos)
def descuentoFinal(sender, instance, **kwargs):
    if instance.pk:
        producto_anterior = sender.objects.get(pk=instance.pk)
        if producto_anterior.descuento != instance.descuento and producto_anterior.precio == instance.precio:
            if instance.PrecioSinDescuento != 0 and instance.descuento != 0:
                descuentoF = (instance.descuento/100)*instance.PrecioSinDescuento
                precioT = instance.PrecioSinDescuento - descuentoF
                instance.precio = precioT
                instance.save()
            elif instance.descuento == 0:
                instance.precio = instance.PrecioSinDescuento
                numeroCero = 0
                instance.PrecioSinDescuento = numeroCero
                instance.save()
            else:
                instance.PrecioSinDescuento = instance.precio
                descuentoF = (instance.descuento/100)*instance.precio
                precioT = instance.precio - descuentoF
                instance.precio = precioT
                instance.save()

@receiver(post_save, sender=Productos)
def Creado(sender, created, instance, **kwargs):
    if created and instance.descuento > 0:
        instance.PrecioSinDescuento = instance.precio
        descuentoF = (instance.descuento/100)*instance.precio
        precioT = instance.precio - descuentoF
        instance.precio = precioT
        instance.save()

@receiver(post_save, sender=LineaPedido)
def actualizar_estado_pedido(sender, instance, **kwargs):
    if instance.estadoPedido in ['Rechazado', 'Pedido entregado']:
        pedido = instance.pedido
        pedido.status = False
        pedido.save()