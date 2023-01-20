from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from collections import Counter
from Aplicaciones.carrito.carro import Carro
from Aplicaciones.pedidos.models import LineaPedido,Pedido
from .models import Categoria,Productos, sliders,comentariosProductos
from .forms import formComentario

user = get_user_model()

#-------------------------Vista del inicio
def index(request):
    template_name = "index.html"
    categoria = Categoria.objects.filter(activo=True)[:5]
    img1 = sliders.objects.all()[:1]
    img2 = sliders.objects.all()[1:]
    productos = Productos.objects.filter(activo=True).order_by('categoria')[:15]
    paginate_by = 15
    context = {
        "productos": productos,
        "categoria":categoria,
        "slider":img1,
        "sliderall":img2,
    }
    return render(request,template_name,context)

#-------------------------Vista categorias
def categoriasDisponibles(request):
    template_name = 'categorias.html'
    categoria = Categoria.objects.filter(activo=True)
    contex = {
        'categoria': categoria
    }
    return render(request,template_name,contex)


#-------------------------Vista de productos por categoría
def buscar_categorias(request,slug):
    template_name = 'list.html'
    nombre_categoria = Categoria.objects.get(slug = slug)
    categoria = Categoria.objects.filter(activo=True)
    productos = Productos.objects.filter(activo=True,categoria = nombre_categoria)
    context = {
        "productos": productos,
        "categoria":categoria,
        "nombreCat":nombre_categoria
    }
    return render(request,template_name,context)

#-------------------------Vista de productos por buscador
def search(request):
    template_name = 'list.html'
    busqueda = request.GET['busqueda']
    categoria = Categoria.objects.filter(activo=True)
    productos = Productos.objects.filter(activo=True, nombre__icontains = busqueda)
    context = {
        "productos": productos,
        "categoria":categoria
    }
    return render(request,template_name,context)


#-------------------------Vista detallada del producto
def detalle(request,producto_id):
    if Productos.objects.filter(activo=True, id = producto_id).exists():
        template_name = 'detal.html'
        #filtro productos
        productos = Productos.objects.filter(activo=True,id = producto_id)
        categoria = Categoria.objects.filter(activo=True)
        pro_id = Productos.objects.get(activo=True,id = producto_id)
        pro_cat_id = pro_id.categoria_id    
        categoria_id = Categoria.objects.get( id=pro_cat_id )
        banner = categoria_id.banner
        comentarios = comentariosProductos.objects.filter(producto_asociado_id = producto_id).order_by('-created_at')

        if request.user.is_authenticated:
            #filtro para POST
            user = request.user.id
            usuario = User.objects.get(id = user)

            #filtro para comentarios
            if request.method == 'POST':
                form = formComentario(request.POST, instance= pro_id )
                form2 = formComentario(request.POST, instance= usuario )
                if form.is_valid() and form2.is_valid() :   
                    coment = request.POST.get('comentario')
                    comentarioF = comentariosProductos.objects.create(comentario = coment, producto_asociado = pro_id, comentario_usuario = usuario)
                    messages.success(request,"Gracias por tu comentario")
                    return redirect('tiendaEnLinea:detail',producto_id) 
            else:
                form = formComentario()

            context = {
                'productos': productos,
                'categoria':categoria,
                'banner':banner,
                'comentarios':comentarios,
                'form':form
            }

        else:
            form = formComentario()

        context = {
            'productos': productos,
            'categoria':categoria,
            'banner':banner,
            'form':form,
            'comentarios':comentarios,
        }

    
    return render(request,template_name,context)

#-------------------------Vista carrito
def mycart(request):
    request.session["paypal"] = False
    template_name = 'carrito/carrito.html'
    return render(request,template_name)



