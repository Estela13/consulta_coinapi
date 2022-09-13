from curses.ascii import isalpha
import requests
from config import apikey

r = requests.get("https://rest.coinapi.io/v1/assets?apikey={}".format(apikey))
if r.status_code != 200:
    raise Exception("Error en consulta de assets: {}".format(r.status_code))

lista_candidatas = r.json()
lista_definitiva = []
for candidata in lista_candidatas:
    #if candidata["type_is_crypto"] == 1:   1 es booleano True, 0 es False
    if candidata["type_is_crypto"]:
        lista_definitiva.append(candidata["asset_id"])


cripto = input("Introduzca una cripto conocida: ").upper()
while cripto != "":
    if cripto in lista_definitiva:
        r = requests.get("https://rest.coinapi.io/v1/exchangerate/{}/EUR?apikey={}".format(cripto, apikey))

        resultado = r.json()
        if r.status_code == 200:
            print("{:.2f} euros".format(resultado["rate"]))
        else:
            print(resultado["error"])
    
    cripto = input("Introduzca una cripto conocida: ").upper()