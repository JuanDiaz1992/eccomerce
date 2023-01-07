import random
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.paginator import Paginator
from django.http import Http404

from Aplicaciones.tiendaEnLinea.models import Productos
from Aplicaciones.carrito.carro import Carro
from .models import Pedido,LineaPedido



def procesar_pedido(request):
    template_name = "carrito/sucess.html"
    pedido = Pedido.objects.create(user = request.user)
    carro = Carro(request)
    lineas_pedido = list()

    for key, value in carro.carro.items():
        pro = Productos.objects.get(id = key)
        pro.stock = int(pro.stock - value["cantidad"])
        pro.save()
        pedido.ordernum = random.randint(10000,99999)
        pedido.save()
        lineas_pedido.append(LineaPedido(
            producto_id = key,
            cantidad = value["cantidad"],
            user = request.user,
            pedido = pedido
        ))
    LineaPedido.objects.bulk_create(lineas_pedido)
    enviar_email(
        pedido = pedido,
        lineas_pedido = lineas_pedido,
        nombreusuario = request.user.username,
        emailusuario = request.user.email
    )
    carro = Carro(request)
    carro.limpiar_carro()
    return redirect('tiendaEnLinea:succes')

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
    page = request.GET.get('page', 1)
    try:
        paginator = Paginator(pedidoUser, 5)
        pedidoUser = paginator.page(page)
    except:
        raise Http404
    contex = {
        'entity':pedidoUser,
        'paginator':paginator

    }
    return render(request,template_name,contex)





