from django.contrib import messages
class Carro:
    def __init__(self, request):
        self.request=request
        self.session=request.session
        carro=self.session.get("carro")

        if not carro:
            carro=self.session["carro"]={}
        #else:
        self.carro=carro
    def agregar(self,producto):
        if(str(producto.id) not in self.carro.keys()):
            self.carro[producto.id]={
                "producto_id":producto.id,
                "nombre":producto.nombre,
                "precio": str(producto.precio),
                "precioInicial": str(producto.precio),
                "descuento": str(producto.descuento),
                "precioSinDescuento": str(producto.PrecioSinDescuento),
                "cantidad":1,
                "stock": producto.stock,
                "imagen":producto.imagen.url,
                "descuento":producto.descuento,
            }
        else:
            for key,value in self.carro.items():
                    if key == str(producto.id) and value["stock"] != value["cantidad"]:
                        value["cantidad"] =  value["cantidad"] + 1
                        value["precio"] =  int(value["precio"]) + producto.precio
                        break
            else:
                return messages.error("error generado a proposito")

        

        self.guardar_carro()
        


    def eliminar(self,producto):
        producto.id = str(producto.id)
        if producto.id in self.carro:
            del self.carro[producto.id]
        self.guardar_carro()


    def restar_producto(self,producto):
        for key,value in self.carro.items():
            if key == str(producto.id):
                value["cantidad"] =  value["cantidad"] - 1
                value["precio"] =  int(value["precio"]) - producto.precio
                if value["cantidad"] < 1:
                    self.eliminar(producto)
                break
        self.guardar_carro()

    def limpiar_carro(self):
        self.session["carro"]={}
        self.session.modified=True





    def guardar_carro(self):
        self.session["carro"] = self.carro
        self.session.modified = True

    



