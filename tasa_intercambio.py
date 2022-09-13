from curses.ascii import isalpha
import requests

apikey = "4A9EEA5C-D6E2-45A3-AF20-58E63D16FAF0"

cripto = input("Introduzca una cripto conocida: ")
while cripto != "":
    if cripto.isalpha():
        r = requests.get("https://rest.coinapi.io/v1/exchangerate/{}/EUR?apikey={}".format(cripto, apikey))

        resultado = r.json()
        if r.status_code == 200:
            print("{:.2f} euros".format(resultado["rate"]))
        else:
            print(resultado["error"])
    
    cripto = input("Introduzca una cripto conocida: ")