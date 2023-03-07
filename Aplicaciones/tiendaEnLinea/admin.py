from django.contrib import admin
from Aplicaciones.Usuarios.models import PerfilUsuario
from Aplicaciones.pedidos.models import Pedido, LineaPedido
from Aplicaciones.tiendaEnLinea.models import Productos,Categoria,sliders, comentariosProductos,Stock


# Register your models here.




admin.site.register(sliders)
admin.site.register(Categoria)


class imagenesP(admin.TabularInline):
    model = Stock
    extra = 0

class stock(admin.TabularInline):
    model = Stock
    extra = 0
    def save_model(self, request, obj, form, change):
    # llama al método save_model de la clase padre
        super().save_model(request, obj, form, change)
    # actualiza el stock total del producto
        obj.producto.stock_total = sum(stock.stock for stock in obj.producto.tallas.all())
        obj.producto.save()




class ProductoAdmin(admin.ModelAdmin):
    list_display = ['nombre','categoria','stock_total','precio']
    search_fields = ['nombre']
    list_filter = ['marca','activo']
    list_per_page: 10

    inlines = [
        stock,
    ]


class detalPedido(admin.TabularInline):
    model = LineaPedido
    extra = 0

class pedidoList(admin.ModelAdmin):
    list_display = ['ordernum','created_at','user','status']
    list_per_page: 10
    search_fields = ['ordernum']
    list_filter = ['status','created_at']
    ordering = ['-created_at']
    inlines =[
        detalPedido,
    ]


    

admin.site.register(Pedido,pedidoList)
admin.site.register(Productos,ProductoAdmin)


admin.site.register([comentariosProductos])

admin.site.register(PerfilUsuario)
