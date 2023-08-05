#Importe las librerias necesarias
import requests as req
import urllib3
#Utilice esta herramienta para quitar un error que me salia al correr el codigo
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
#Escogi la usar esta informacion porque el juego pokemon fue parte importante de mi infancia
#me parecio interesante toda la info sobre cada uno de los pokemones de todas las generaciones
#
#Hice una variable con el valor del URL del API para comodidad al escribir el codigo
PokeApi = "https://pokeapi.co/api/v2"


#Esta funcion nos devuelve todos los pokemones de la generacion solicitada.
def gen_pokemon(generation):
    url_gen = f"https://pokeapi.co/api/v2/generation/{generation}"
    response = req.get(url_gen)

    if response.status_code == 200:
        datagen = response.json()
        lista_poke = datagen["pokemon_species"]

        print(f"Estos son los pokemones de la generacion {generation}:")
        for pokemon in lista_poke:
            print(pokemon["name"])
    else:
        print("Error")

#Esta funcion nos devuelve un URL de una imagen del pokemon solicitado.
def imag_poke(pokemon_name):
    url_imag = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}"
    response = req.get(url_imag)

    if response.status_code == 200:
        dataimag = response.json()
        imagen_url = dataimag["sprites"]["front_default"]
        return imagen_url
    else:
       print("Imagen no disponible.")


#Esta funcion nos devuelven datos del pokemon, esta me parecio muy interesante porque tenia
#que buscar varia info para mostrar al mismo tiempo como
#el nombre de la data(defensa, ataque, y otros) y su valor
def est_pokemon(pokemon_name):
    urlestatus = f"{PokeApi}/pokemon/{pokemon_name.lower()}"
    response = req.get(urlestatus, verify=False)

    if response.status_code == 200:
        datapoke = response.json()
        datos = datapoke["stats"]
        for stat in datos:
            stat_name = stat["stat"]["name"]
            stat_value = stat["base_stat"]
            print(f"- {stat_name}: {stat_value}")
    else:
        print("Error")


#Esta funcion unicamente de devuelve el tipo de pokemon.
def tipo_pokemon(pokemon_name):
    urltipo_poke = f"{PokeApi}/pokemon/{pokemon_name.lower()}"
    response = req.get(urltipo_poke, verify=False)

    if response.status_code == 200:
        datapoke = response.json()
        tipos = datapoke["types"]
        for tipo in tipos:
            tipo_poke = tipo["type"]["name"]
            print(tipo_poke)
    else:
        print("Error")


#Esta funcion me devuelve las habilidades que tenga el pokemon
def habil_pokemon(pokemon_name):
    urlHabil = f"{PokeApi}/pokemon/{pokemon_name.lower()}"
    response = req.get(urlHabil, verify=False)

    if response.status_code == 200:
        datapoke = response.json()
        habilidades = datapoke["abilities"]
        
        print(f"Las habilidades de {pokemon_name.capitalize()} son:")
        for habilidad in habilidades:
            pokehabil = habilidad["ability"]["name"]
            print(pokehabil)

#Esta funcion es bastante sencilla ya que unicamente devuelve el valor de la altura del pokemon.
def poke_altura(pokemon_name):
    url_altura = f"{PokeApi}/pokemon/{pokemon_name.lower()}"
    response = req.get(url_altura, verify=False)

    if response.status_code == 200:
        alturas = response.json()
        altu_poke = alturas["height"]
        print(f"La altura de {pokemon_name.capitalize()} es de {altu_poke} meters.")
    else:
        print("Error")



#Esta funcion es bastante sencilla tambien ya que igual a la anterior,
#esta unicamente devuelve el peso del pokemon.
def peso_pokemon(pokemon_name):
    url_peso = f"{PokeApi}/pokemon/{pokemon_name.lower()}"
    response = req.get(url_peso, verify=False)

    if response.status_code == 200:
        pesos = response.json()
        peso_poke = pesos["weight"]
        print(f"El peso de {pokemon_name.capitalize()} es de {peso_poke} kilograms")



  

