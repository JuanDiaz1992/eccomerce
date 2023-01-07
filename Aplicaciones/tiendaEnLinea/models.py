from django.db import models
from autoslug import AutoSlugField
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver

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

class Productos(models.Model):
    codigo = models.CharField(max_length=10)
    nombre=models.CharField(max_length=250)
    slug=AutoSlugField(populate_from ='codigo')
    imagen= models.ImageField(upload_to = 'img/Productos' , default='static/img/logo.png', null= True, blank=True)
    marca=models.CharField(max_length=250)
    descripcion=models.TextField(blank=True,null=True)
    precio=models.IntegerField(default=0)
    descuento = models.IntegerField(default=0,blank=True,null=True)
    PrecioSinDescuento = models.IntegerField(default=0,blank=True,null=True)
    categoria=models.ForeignKey(Categoria,on_delete=models.CASCADE)
    destacado=models.BooleanField(default=True)
    activo= models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    stock = models.IntegerField(default=1)


    def __str__(self) -> str:
        return self.nombre

    class Meta:
        verbose_name_plural='Producto'





class imagenesProductos(models.Model):
    imagen= models.ImageField(upload_to = 'img/Productos')
    producto = models.ForeignKey(Productos, on_delete=models.CASCADE, related_name='imagenes')
    

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



@receiver(post_save, sender=Productos)
def descuentoFinal(sender,created, **kwargs):
    codigoTemp = kwargs["instance"]
    #pro = Productos.objects.get(codigo = codigoTemp.codigo)
    print(codigoTemp)
    if created:
        if codigoTemp.descuento > 0:
            descuentoF = (codigoTemp.descuento/100)*codigoTemp.precio
            precioT = codigoTemp.precio - descuentoF
            codigoTemp.PrecioSinDescuento = codigoTemp.precio
            codigoTemp.precio = precioT
            codigoTemp.save()


