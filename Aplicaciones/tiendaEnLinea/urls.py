from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required

from .views import index,buscar_categorias,search,detalle,mycart,categoriasDisponibles
from Aplicaciones.Usuarios.views import Login, LogoutUsuario, register, modificarPerUsuario
from Aplicaciones.pedidos.views import procesar_pedido,pedidoFinalizado,listaPedidosUsuario,detallePedido
from Aplicaciones.carrito.views import agregar_producto,eliminar_producto,restar_producto,limpiar_carro,agregar_desde_detalle



app_name='tiendaEnLinea'


urlpatterns = [
    path('',index, name= 'index'),
    path('categorias/<slug>',buscar_categorias, name= 'categorias'),
    path('search',search, name= 'search'),
    path('detalle/<int:producto_id>',detalle, name= 'detail'),
    path('categorias/',categoriasDisponibles, name= 'categorias'),
    #carrito
    path('mycart/',login_required(mycart), name= 'mycart'),
    path('agregar/<int:producto_id>/<str:color>/<str:talla>/',login_required(agregar_producto), name= 'agregar'),
    path('agregarDetalle/',agregar_desde_detalle, name= 'agregarDetalle'),
    path('eliminar/<int:producto_id>/<str:color>/<str:talla>/',eliminar_producto, name= 'eliminar'),
    path('restar/<int:producto_id>/<str:color>/<str:talla>/',restar_producto, name= 'restar'),
    path('limpiar/',limpiar_carro, name= 'limpiar'), 

    
    #Gestión usuarios
    path('accounts/login/',Login.as_view(), name = 'login'),
    path('register/',register, name = 'register'),
    path('logout/',login_required(LogoutUsuario), name = 'logout'),
    path('modPerfUs/', modificarPerUsuario, name ='ModificarPerfil'),
    

    #procesar pedido
    path('pedidoProcesado/',login_required(procesar_pedido), name = 'pedidoProcesado'),
    path('listaPedidos/',login_required(listaPedidosUsuario), name = 'listaPedidosUsuario'),
    path('succes/',login_required(pedidoFinalizado), name = 'succes'),
    path('detallePedido/<int:pedido_id>',login_required(detallePedido), name = 'detallePedido'),


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)