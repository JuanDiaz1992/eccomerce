from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import messages

from .carro import Carro
from Aplicaciones.tiendaEnLinea.models import Categoria
from Aplicaciones.tiendaEnLinea.models import Productos,imagenesProductos


# Create your views here.


def agregar_desde_detalle(request):
    carro = Carro(request)
    if request.method == 'POST':
        id = request.POST['id']
        producto = Productos.objects.get(id = id)
        color = request.POST['color']
        img2 = imagenesProductos.objects.get(id = color)
        img = img2.imagen
        colorProducto = img2.colores
        try:
            talla = request.POST['talla']
        except:
            talla = "Estandar"
            
        try:
            carro.agregar(producto = producto, imagen = img, color = colorProducto, talla = talla)
            messages.success(request,"Producto agregado al carrito")
        except:
            messages.error(request,"Ya agregaste las existencias disponibles de este producto")

    return redirect('tiendaEnLinea:detail',id) 


def agregar_producto(request,producto_id):
    img3 = imagenesProductos.objects.filter(producto_id = producto_id)[:1]
    img2 = imagenesProductos.objects.get(id = img3)
    img = img2.imagen
    color =""
    talla = ""
    carro = Carro(request)
    producto = Productos.objects.get(id = producto_id)
    carro.agregar(producto = producto, imagen = img, color = color, talla = talla )
    
    return redirect("tiendaEnLinea:mycart")



def eliminar_producto(request, producto_id):
    carro = Carro(request)
    producto = Productos.objects.get(id = producto_id)
    carro.eliminar(producto = producto)
    return redirect("tiendaEnLinea:index")


def restar_producto(request, producto_id):
    carro = Carro(request)
    producto = Productos.objects.get(id = producto_id)
    carro.restar_producto(producto = producto)
    return redirect("tiendaEnLinea:mycart")

def limpiar_carro(request):
    carro = Carro(request)
    carro.limpiar_carro()
    return redirect("tiendaEnLinea:index")



    