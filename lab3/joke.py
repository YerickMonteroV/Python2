 #1.crear una funcion que devuelva un chiste aleatorio.
 #2.crear una funcion que muestre la lista de las categorias disponibles 
 #   y la opcion de elegir .
 #3.crear una funcion que muestre el chiste de la categoria seleccionada. 
 #4.crear un menu donde el usuario puede utilizar las opciones como plazca.


#importamos las galerias necesarias
import requests as req

#Esta funcion nos seleciona un chiste al azar
def Ramdonjoke():
    urlRam = "https://api.chucknorris.io/jokes/random"
    getResp = req.get(urlRam)

    if getResp.status_code == 200:
        data= getResp.json()
        print(data["value"])

#Esta funcion nos muestra las categorias de chistes disponibles
def Categojoke():
    urlCat = "https://api.chucknorris.io/jokes/categories"
    getResp = req.get(urlCat)

    if getResp.status_code == 200:
        data= getResp.json()
        print("Las categorias disponibles son:")
        for selec in data:
            print(selec)

#Esta funcion nos muesta un chiste de acuerdo con la categoria
# seleccionada por el usuario   
def Selecjoke(x):
    category=x
    urlSelec = f"https://api.chucknorris.io/jokes/random?category={category}"
    getResp = req.get(urlSelec)

    if getResp.status_code == 200:
        data= getResp.json()
        print(data["value"])

