from django.contrib import admin
from Aplicaciones.Usuarios.models import PerfilUsuario
from Aplicaciones.pedidos.models import Pedido, LineaPedido
from Aplicaciones.tiendaEnLinea.models import Productos,Categoria,sliders, comentariosProductos, imagenesProductos,tallaProductos


# Register your models here.




admin.site.register(sliders)
admin.site.register(Categoria)

"""
class ImagenProductoAdmin(admin.TabularInline):
    model = imagenesProductos
"""

class imagenesP(admin.TabularInline):
    model = imagenesProductos
    extra = 1

class TallP(admin.TabularInline):
    model = tallaProductos
    extra = 1

class detalPedido(admin.TabularInline):
    model = LineaPedido
    extra = 0

class ProductoAdmin(admin.ModelAdmin):
    list_display = ['nombre','categoria','stock','precio']
    list_editable = ['precio','stock']
    search_fields = ['nombre']
    list_filter = ['marca','activo']
    list_per_page: 10
    inlines = [
        imagenesP,
        TallP,
    ]

class pedidoList(admin.ModelAdmin):
    list_display = ['ordernum','user','status']
    list_per_page: 10
    search_fields = ['ordernum']
    inlines =[
        detalPedido,
    ]


    

admin.site.register(Pedido,pedidoList)
admin.site.register(Productos,ProductoAdmin)


admin.site.register([comentariosProductos])

admin.site.register(PerfilUsuario)