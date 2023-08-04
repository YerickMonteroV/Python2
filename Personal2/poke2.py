#Importe las librerias necesarias
import requests as req
import urllib3
#Utilice esta herramienta para quitar un error que me salia al correr el codigo
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
#Escogi la usar esta informacion porque me 
#
#Hice una variable con el valor del URL del API para comodidad al escribir el codigo
PokeApi = "https://pokeapi.co/api/v2"
#Function for pokemon stats

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


#Function for pokemon type

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


#Function pokemon abilities

def habil_pokemon(pokemon_name):
    urlHabil = f"{PokeApi}/pokemon/{pokemon_name.lower()}"
    response = req.get(urlHabil, verify=False)

    if response.status_code == 200:
        datapoke = response.json()
        habilidades = datapoke["abilities"]
        
        print(f"Las abilidades {pokemon_name.capitalize()} abilities:")
        for habilidad in habilidades:
            pokehabil = habilidad["ability"]["name"]
            print(pokehabil)


#Function of pokemon height

def alt_pokemon(pokemon_name):
    url_poke_height = f"{PokeApi}/pokemon/{pokemon_name.lower()}"
    height_response = req.get(url_poke_height, verify=False)

    if height_response.status_code == 200:
        height_details = height_response.json()
        height_decimeters = height_details["height"]
        height = height_decimeters / 10  # Convert decimeters to meters
        print(f"The height of {pokemon_name.capitalize()} is: {height} meters.")
    else:
        print(f"No se pudo obtener la información del Pokémon {pokemon_name.capitalize()}.")



#Function for pokemon weight

def peso_pokemon(pokemon_name):
    url_poke_weight = f"{PokeApi}/pokemon/{pokemon_name.lower()}"
    weight_response = req.get(url_poke_weight, verify=False)

    if weight_response.status_code == 200:
        weight_details = weight_response.json()
        weight_hectograms = weight_details["weight"]
        weight = int(weight_hectograms / 10) # Convert hectograms to kilograms
        print(f"The weight of {pokemon_name.capitalize()} is : {weight} kilograms")




def gen_pokemon(generation):
    url = f"https://pokeapi.co/api/v2/generation/{generation}"
    response = req.get(url)

    if response.status_code == 200:
        data = response.json()
        pokemon_list = data["pokemon_species"]

        print(f"Listado de Pokémon en la generación {generation}:")
        for pokemon in pokemon_list:
            print(pokemon["name"])
    else:
        print(f"Error al obtener datos de la generación {generation}. Código de estado: {response.status_code}")




def imag_pokemon(pokemon_name):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}"
    response = req.get(url)

    if response.status_code == 200:
        data = response.json()
        image_url = data["sprites"]["front_default"]
        return image_url
    else:
       return f"El Pokémon {pokemon_name} no tiene una imagen disponible."
  

