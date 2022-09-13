from criptoexchange.models import Cambio, TodoCoinApiIO, ModelError
from config import apikey

todas = TodoCoinApiIO()
todas.trae(apikey)

print("{} de {}".format(len(todas.criptos), len(todas.criptos) + len (todas.no_criptos)))

cripto = input("introduzca una cripto conocida: ").upper()
while cripto != "" :
    if cripto in todas.criptos:
        tipoCambio = Cambio(cripto)
        try:
            tipoCambio.actualiza(apikey)

            print("{:.2f} €".format(tipoCambio.tasa))
        except ModelError as variable:
            print("Se ha producido el error {}".format(variable))

    cripto = input("introduzca una cripto conocida: ").upper()