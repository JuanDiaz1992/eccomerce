from django.db import models
from django.contrib.auth import get_user_model
from Aplicaciones.tiendaEnLinea.models import Productos
from django.db.models import F,Sum,FloatField
from .choices import estado

User = get_user_model()

# Create your models here.
class Pedido(models.Model):
    ordernum = models.CharField(max_length=9,null=True,blank=True)
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.ordernum


    @property
    def total(self):
        return self.LineaPedido_set.aggregate(
            total = Sum(F("precio")*F("cantidad"), output_field = FloatField())
        )["total"]
        

    class Meta:
        db_table = 'pedidos'
        verbose_name = 'pedido'
        verbose_name_plural = 'pedidos'
        ordering = ['created_at']

class LineaPedido(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    producto = models.ForeignKey(Productos, on_delete= models.CASCADE)
    pedido = models.ForeignKey(Pedido, on_delete= models.CASCADE)
    cantidad = models.IntegerField(default=1)
    estadoPedido = models.CharField(max_length=50,choices = estado, default = 'Aceptado')
    
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f'{self.cantidad} unidades de {self.producto.nombre}'

    class Meta:
        db_table = 'Lineapedidos'
        verbose_name = 'Linea pedido'
        verbose_name_plural = 'Lineas pedidos'
        ordering = ['created_at']