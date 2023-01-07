from .carro import Carro
def importe_total_carro(request):
    carro = Carro(request)
    total = 0
    CantTotal = 0
    if request.user.is_authenticated:
        for key, value in request.session["carro"].items():
            total = total + int(value["precio"])
            CantTotal = CantTotal + int(value["cantidad"])
    return{"importe_total_carro":total,"importe_CantTotal_carro":CantTotal}