from django.contrib import messages
class Carro:
    def __init__(self, request):
        self.request=request
        self.session=request.session
        carro=self.session.get("carro")

        if not carro:
            carro=self.session["carro"]={}
        self.carro=carro

    def agregar(self,producto,imagen,color,talla):
        clave = f"{producto.id}-{color}-{talla}"
        if clave not in self.carro.keys():
            self.carro[clave]={
                "producto_id":producto.id,
                "nombre":producto.nombre,
                "precio": producto.precio,
                "precioInicial": str(producto.precio),
                "descuento": str(producto.descuento),
                "precioSinDescuento": str(producto.PrecioSinDescuento),
                "cantidad":1,
                "imagen":imagen.url,
                "stock": producto.stock,
                "color": color,
                "talla": talla,
                "descuento":producto.descuento,
            }
        else:
            for key,value in self.carro.items():
                if key == clave and value["stock"] != value["cantidad"]:
                    value["cantidad"] += 1
                    value["precio"] += producto.precio
                    break
            else:
                messages.error(self.request,"Ya agregaste las existencias disponibles de este producto")

        self.guardar_carro()

        



    def eliminar(self,producto, color, talla):
        producto_id = str(producto.id) + '_' + color + '_' + talla
        if producto_id in self.carro:
            del self.carro[producto_id]
        self.guardar_carro()

    def restar_producto(self,producto, color, talla):
        producto_id = str(producto.id) + '_' + color + '_' + talla
        for key,value in self.carro.items():
            if key == producto_id:
                value["cantidad"] =  value["cantidad"] - 1
                value["precio"] =  int(value["precio"]) - producto.precio
                if value["cantidad"] < 1:
                    self.eliminar(producto, color, talla)
                break
        self.guardar_carro()

    def limpiar_carro(self):
        self.session["carro"]={}
        self.session.modified=True

    def guardar_carro(self):
        self.session["carro"] = self.carro
        self.session.modified = True





    def guardar_carro(self):
        self.session["carro"] = self.carro
        self.session.modified = True

    



