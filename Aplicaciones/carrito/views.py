from django.shortcuts import render
from django.shortcuts import redirect

from django.http import JsonResponse

from .context_processor import importe_total_carro

from .carro import Carro
from Aplicaciones.tiendaEnLinea.models import Categoria
from Aplicaciones.tiendaEnLinea.models import Productos,imagenesProductos,tallaProductos

def agregar_desde_detalle(request):

    carro = Carro(request)
    

    if request.method == 'POST':
        id = request.POST['id']
        producto = Productos.objects.get(id=id)
        color = request.POST['color']
        img2 = imagenesProductos.objects.get(id=color)
        img = img2.imagen
        colorProducto = img2.colores
        talla = request.POST['talla']
        stock_talla = tallaProductos.objects.get(producto = id,tallas = talla )
        resultado = carro.agregar(producto=producto, imagen=img, color=colorProducto, talla=talla, stock = stock_talla.stock)
        if resultado:
            mensaje = True
        else:
            mensaje = False
            
        if request.is_ajax():
            importe = importe_total_carro(request) 
            context = importe["importe_CantTotal_carro"]
            data = context
            
            return JsonResponse ({
                'data':data,
                'producto':str(producto.nombre),
                'color':colorProducto,
                'talla': talla,
                'mensaje': mensaje
            })
        
    return redirect('tiendaEnLinea:detail',id) 



def agregar_producto(request,producto_id,color,talla):
    img3 = imagenesProductos.objects.filter(producto_id = producto_id)[:1]
    img2 = imagenesProductos.objects.get(id = img3)
    img = img2.imagen
    stock_talla = tallaProductos.objects.get(producto = producto_id,tallas = talla )
    colorITem = color
    tallaItem = talla
    carro = Carro(request)
    producto = Productos.objects.get(id = producto_id)
    carro.agregar(producto=producto, imagen=img, color=colorITem, talla=tallaItem, stock = stock_talla.stock)
    
    return redirect("tiendaEnLinea:mycart")


def eliminar_producto(request, producto_id,color,talla):
    carro = Carro(request)
    clave = f"{producto_id}-{color}-{talla}"
    carro.eliminar(clave=clave)
    return redirect("tiendaEnLinea:index")

def restar_producto(request, producto_id,color,talla):
    carro = Carro(request)
    colorITem = color
    tallaItem = talla
    producto = Productos.objects.get(id=producto_id)
    carro.restar_producto(producto=producto,color=colorITem, talla=tallaItem)
    return redirect("tiendaEnLinea:mycart")

def limpiar_carro(request):
    carro = Carro(request)
    carro.limpiar_carro()
    return redirect("tiendaEnLinea:index")