from django.contrib import messages
class Carro:
    def __init__(self, request):
        self.request=request
        self.session=request.session
        carro=self.session.get("carro")
        if not carro:
            carro=self.session["carro"]={}
        self.carro=carro
    def agregar(self,producto,imagen,color,talla,stock):
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
                "stock": stock,
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
                return False
        self.guardar_carro()
        return True


    def eliminar(self, producto, color, talla):
        clave = f"{producto.id}-{color}-{talla}"
        copia_carro = dict(self.carro)
        for key, value in copia_carro.items():
            if key == clave:
                del self.carro[clave]  
        self.guardar_carro()


    def restar_producto(self,producto, color, talla):
        clave = f"{producto.id}-{color}-{talla}"
        for key,value in self.carro.items():
            if key == clave:
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


