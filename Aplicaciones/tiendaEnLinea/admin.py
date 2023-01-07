from django.contrib import admin
from Aplicaciones.Usuarios.models import PerfilUsuario
from Aplicaciones.pedidos.models import Pedido, LineaPedido
from Aplicaciones.tiendaEnLinea.models import Productos,Categoria, imagenesProductos,sliders, comentariosProductos


# Register your models here.


admin.site.register(PerfilUsuario)

admin.site.register(sliders)
admin.site.register(Categoria)

class ImagenProductoAdmin(admin.TabularInline):
    model = imagenesProductos


class ProductoAdmin(admin.ModelAdmin):
    list_display = ['nombre','categoria','precio']
    list_editable = ['precio']
    search_fields = ['nombre']
    list_filter = ['marca','activo']
    list_per_page: 10
    inlines = [
        ImagenProductoAdmin
    ]

class pedidoList(admin.ModelAdmin):
    list_display = ['ordernum','user','status']
    list_per_page: 10
    search_fields = ['ordernum']

class pedidoListDetalle(admin.ModelAdmin):
    list_display = ['pedido','estadoPedido','producto','cantidad','user']
    list_editable = ['estadoPedido']
    list_filter = ['estadoPedido','user']
    list_per_page: 10
    search_fields = ['pedido']
    

admin.site.register(Pedido,pedidoList)
admin.site.register(Productos,ProductoAdmin)
admin.site.register(LineaPedido,pedidoListDetalle)

admin.site.register([comentariosProductos])

