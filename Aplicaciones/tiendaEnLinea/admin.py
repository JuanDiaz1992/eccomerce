from django.contrib import admin
from Aplicaciones.Usuarios.models import PerfilUsuario
from Aplicaciones.pedidos.models import Pedido, LineaPedido
from Aplicaciones.tiendaEnLinea.models import Productos,Categoria,sliders, comentariosProductos, imagenesProductos,tallaProductos


# Register your models here.




admin.site.register(sliders)
admin.site.register(Categoria)


class imagenesP(admin.TabularInline):
    model = imagenesProductos
    extra = 1

class TallP(admin.TabularInline):
    model = tallaProductos
    extra = 0
    def save_model(self, request, obj, form, change):
    # llama al método save_model de la clase padre
        super().save_model(request, obj, form, change)
    # actualiza el stock total del producto
        obj.producto.stock_total = sum(talla.stock for talla in obj.producto.tallas.all())
        obj.producto.save()


class detalPedido(admin.TabularInline):
    model = LineaPedido
    extra = 0

class ProductoAdmin(admin.ModelAdmin):
    list_display = ['nombre','categoria','stock_total','precio']
    list_editable = ['precio']
    search_fields = ['nombre']
    list_filter = ['marca','activo']
    list_per_page: 10
    def get_readonly_fields(self, request, obj=None):
        # Retorna una lista de campos de solo lectura
        if obj:
            return ['stock_total']  # El campo stock_total será de solo lectura cuando se edite un objeto existente
        else:
            return []  # El campo stock_total no será de solo lectura cuando se cree un nuevo objeto

    def stock_total(self, obj):
        return obj.stock_total
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