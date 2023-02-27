from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.core import serializers
from collections import Counter
from Aplicaciones.carrito.carro import Carro
from Aplicaciones.pedidos.models import LineaPedido,Pedido
from .models import Categoria,Productos, sliders,comentariosProductos
from .forms import formComentario

user = get_user_model()



#-------------------------Vista del inicio
def index(request):
    template_name = "index.html"
    categoria = Categoria.objects.filter(activo=True)
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
    marcas = productos.values_list('marca', flat=True).distinct()
    sexo = productos.values_list('sexo', flat=True).distinct()

    context = {
        "productos": productos,
        "categoria":categoria,
        "nombreCat":nombre_categoria,
        "marcas":marcas,
        "sexo":sexo
    }
    return render(request,template_name,context)


#-------------------------FiltrarCategoria
def filtrarCategoria(request):
    if request.method == 'POST':
        
        marcaFiltro = request.POST.get('marca')
        generoFiltro = request.POST['genero']

        if generoFiltro == "todos":
            productoFiltrado = Productos.objects.filter(marca=marcaFiltro)
        elif marcaFiltro is None:
            productoFiltrado = Productos.objects.filter(sexo=generoFiltro)

        else:
            productoFiltrado = Productos.objects.filter(marca=marcaFiltro, sexo=generoFiltro)
        productos = []
        for producto in productoFiltrado:
            producto_dict = {
                'id': producto.id,
                'codigo': producto.codigo,
                'nombre': producto.nombre,
                'marca': producto.marca,
                'imagen': producto.obtener_imagen(id_producto=producto.id),
                'precio': producto.precio,
                'precioSinDescuento':producto.PrecioSinDescuento,
                'descuento':producto.descuento
            }
            productos.append(producto_dict)
            print(productos)

        
        if request.is_ajax():
            return JsonResponse ({
                'marca':marcaFiltro,
                'genero':generoFiltro,
                'productos':productos
            })

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
    template_name = 'carrito/carrito.html'
    return render(request,template_name)



