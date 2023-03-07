from django.db import models
from django.contrib.auth import get_user_model
from .choices import color,tallas,sexo
from autoslug import AutoSlugField
import os




User = get_user_model()

class Categoria (models.Model):
    nombre= models.CharField(max_length=250)
    slug=AutoSlugField(populate_from ='nombre')
    activo= models.BooleanField(default=True)
    imagen= models.ImageField(upload_to = 'img/Categorías' , null= True, blank=True)
    banner = models.ImageField(upload_to = 'img/Categorías/banner', default='static/img/banner.jpg' , null= True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.nombre
    
    class Meta:
        verbose_name_plural='Categoria'
    def delete(self, *args, **kwargs):
        # Eliminar la imagen correspondiente si existe
        if self.imagen:
            os.remove(self.imagen.path)
        super().delete(*args, **kwargs)



class Productos(models.Model):
    codigo = models.CharField(max_length=10)
    nombre=models.CharField(max_length=70)
    slug=AutoSlugField(populate_from ='codigo')
    marca=models.CharField(max_length=250)
    descripcion=models.TextField(blank=True,null=True)
    precio=models.IntegerField(default=0)
    descuento = models.IntegerField(default=0,blank=True,null=True)
    PrecioSinDescuento = models.IntegerField(default=0,blank=True,null=True)
    categoria=models.ForeignKey(Categoria,on_delete=models.CASCADE)
    destacado=models.BooleanField(default=True)
    activo= models.BooleanField(default=True)
    stock_total = models.IntegerField(default=0)
    sexo = models.CharField(max_length=20, choices=sexo, default='No definido', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)



    def obtener_imagen(self,id_producto, color, talla):
        imagen = self.stock.filter(producto_id = id_producto, colores=color, tallas=talla).first()
        if imagen:
            return imagen.imagen.url
        return ''

    def __str__(self) -> str:
        return self.nombre

    class Meta:
        verbose_name_plural='Producto'


class Stock(models.Model):
    producto = models.ForeignKey(Productos, on_delete=models.CASCADE, related_name='stock')
    tallas = models.CharField(max_length=50, choices=tallas, default='Talla Unica')
    colores = models.CharField(max_length=50, choices= color,default= '',blank=True,null=True)
    stock = models.IntegerField(default=1)
    imagen= models.ImageField(upload_to = 'img/Productos', default='static/img/logo.png', null= True, blank=True)

    def delete(self, *args, **kwargs):
        # Eliminar la imagen correspondiente si existe
        if self.imagen:
            os.remove(self.imagen.path)
        super().delete(*args, **kwargs)




class comentariosProductos(models.Model):
    comentario = models.CharField(max_length=250,blank=True,null=True)
    producto_asociado = models.ForeignKey(Productos, on_delete=models.CASCADE,)
    comentario_usuario = models.ForeignKey(User,null=True, blank=True, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True,null=True, blank=True)
    def __str__(self) -> str:
        return self.comentario

class sliders(models.Model):
    sliderImg= models.ImageField(upload_to = 'img/Sliders',default='static/img/Slider1.png')
    nombreBanner=models.CharField(max_length=250)

    def __str__(self) -> str:
        return self.nombreBanner
    class Meta:
        verbose_name_plural='Sliders'






def choiceadapter(enumtype):
    return ((item.value, item.name.replace('_', ' ')) for item in enumtype)
