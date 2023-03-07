import random
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from Aplicaciones.Usuarios.models import PerfilUsuario
from django.contrib import messages
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.paginator import Paginator
from django.http import Http404




from Aplicaciones.tiendaEnLinea.models import Productos,Stock
from Aplicaciones.carrito.carro import Carro
from Aplicaciones.carrito.context_processor import importe_total_carro
from .models import Pedido,LineaPedido
from .form import formEnvio


#-------------------------Vista geradora de pedido
def procesar_pedido(request):
    template_name = "carrito/formEnvio.html"
    carro = Carro(request)
    lineas_pedido = list()


    if request.method == 'POST':
        form = formEnvio(request.POST)
        if form.is_valid(): 
            pedido = Pedido.objects.create(user = request.user)
            for clave, value in carro.carro.items():
                clave_split = clave.split("-")
                pro = Productos.objects.get(id=clave_split[0])
                color = clave_split[1]
                talla = clave_split[2]
                talla_stock =  Stock.objects.get(producto = pro.id, tallas = talla, colores =color)
                #datos obtenidos del formulario
                dir = form.cleaned_data['direccion']
                depart = form.cleaned_data['departamento']
                ciudad = form.cleaned_data['ciudad']
                cel = form.cleaned_data['celular']
                cedula = form.cleaned_data['cedula']
                comentarios = form.cleaned_data['comentarios']

                #reducción del stock del producto:
                talla_stock.stock = int(talla_stock.stock - value["cantidad"])
                talla_stock.save()

                #procesado de datos para el envío:
                #dato del costo total de la compra:
                total = importe_total_carro(request)

                pedido.cedula = cedula
                pedido.celular = cel
                pedido.direccion = dir
                pedido.departamento = depart
                pedido.ciudad = ciudad
                pedido.ordernum = random.randint(10000, 99999)
                pedido.precioTotal = total['importe_total_carro']
                pedido.comentarios = comentarios
                pedido.save()

                lineas_pedido.append(LineaPedido(
                    producto=pro,
                    cantidad=value["cantidad"],
                    precioUnidad=int(value["precioInicial"]),
                    user=request.user,
                    pedido=pedido,
                    subTotal=value["precio"],
                    color=color,
                    talla=talla
                ))
            try:
            #uso de función para envió de correo:
                LineaPedido.objects.bulk_create(lineas_pedido)
                enviar_email(
                    color=color,
                    talla=talla,
                    pedido=pedido,
                    lineas_pedido=lineas_pedido,
                    nombreusuario=request.user.username,
                    emailusuario=request.user.email
                )
                carro.limpiar_carro()
                messages.success(request, '¡Gracias por su compra!')
                return redirect('tiendaEnLinea:succes')
            except:
                carro = Carro(request)
                carro.limpiar_carro()
                return redirect('tiendaEnLinea:succes')
            
    else:
        user = request.user.id
        us = PerfilUsuario.objects.get(user_id = user)  
        form=formEnvio(instance = us)
    context={
            'form':form,
        }
    return render (request,template_name, context)



#-------------------------Vista para envio de correo

def enviar_email(**kawargs): 
    asunto = "Gracias por tu pedido"
    mensaje = render_to_string("emails/pedido.html",{
        "pedido":kawargs.get("pedido"),
        "lineas_pedido": kawargs.get("lineas_pedido"),
        "nombreusuario": kawargs.get("nombreusuario")
    })
    mensaje_texto = strip_tags(mensaje)
    from_email = "juannavegante2010@gmail.com"
    to = kawargs.get("emailusuario")
    send_mail(asunto,mensaje_texto,from_email,[to],html_message=mensaje)


#-------------------------Vista pedido creado con exito
def pedidoFinalizado(request):
    template_name = 'carrito/sucess.html'
    pedido = Pedido.objects.filter(user = request.user).order_by("-created_at")[0]
    contex = {
        'pedido':pedido
    }
    return render(request,template_name,contex)



#-------------------------Vista historial pedidos
def listaPedidosUsuario(request):
    template_name = "carrito/listaPedidos.html"
    
    idUsuario = request.user.id
    pedidoUser = LineaPedido.objects.filter(user = idUsuario).order_by("-created_at")
    pedidos_con_imagenes = []
    for pedido in pedidoUser:
        imagen = pedido.producto.obtener_imagen(pedido.producto_id,pedido.color, pedido.talla)
        pedidos_con_imagenes.append({
            'imagen':imagen,
            'pedido':pedido,
        })
    page = request.GET.get('page', 1)
    try:
        paginator = Paginator(pedidos_con_imagenes, 5)
        pedidos_con_imagenes = paginator.page(page)
    except:
        raise Http404
    contex = {
        'entity':pedidos_con_imagenes,
        'paginator':paginator

    }
    return render(request,template_name,contex)


#-------------------------Vista detalle pedido

def detallePedido(request,pedido_id):
    template_name = "carrito/pDetalle.html"
    pedidoDetalle = LineaPedido.objects.filter(pedido_id = pedido_id)
    pedidoF = Pedido.objects.get(id = pedido_id)
    pedidos_con_imagenes = []
    for pedido in pedidoDetalle:
        imagen = pedido.producto.obtener_imagen(pedido.producto_id,pedido.color, pedido.talla)
        pedidos_con_imagenes.append({
            'imagen': imagen,
            'pedido':pedido
        })
    contex = {

        'pedidoD': pedidos_con_imagenes,
        'fechaCompra': pedidoF.created_at,
        'referencia':pedidoF.ordernum,
        'pedidoF':pedidoF.precioTotal,
        'direccion':pedidoF.direccion,
        'ciudad': pedidoF.ciudad,
        'departamento': pedidoF.departamento.lower(),
        'comentarios': pedidoF.comentarios,

    }
    return render(request,template_name,contex)



