import requests as req
import urllib3

#A base URL will be created in order to call this variable in the functions created

BASE_URL = "https://pokeapi.co/api/v2"
pokemon = input("Provide pokemon name: ")

#Function for pokemon stats

def pokemon_stats(pokemon_name):
    url_poke_stats = f"{BASE_URL}/pokemon/{pokemon_name.lower()}"
    response = req.get(url_poke_stats, verify=False)

    if response.status_code == 200:
        stats_details = response.json()
        stats = stats_details["stats"]

        print(f"Stats de {pokemon_name.capitalize()}:")
        for stat in stats:
            stat_name = stat["stat"]["name"]
            stat_value = stat["base_stat"]
            print(f"- {stat_name}: {stat_value}")
    else:
        print(f"No se pudo obtener la información del Pokémon {pokemon_name.capitalize()}.")


#Function for pokemon type

def pokemon_type(pokemon_name):
    url_poke_type = f"{BASE_URL}/pokemon/{pokemon_name.lower()}"
    response = req.get(url_poke_type, verify=False)

    if response.status_code == 200:
        type_details = response.json()
        types = type_details["types"]["name"]
        print(types)


        #print(f"Tipos de {pokemon_name.capitalize()}:")
       # for poke_type in types:
           # type_name = poke_type["type"]["name"]
           # print(f"- {type_name}")
    else:
        print(f"No se pudo obtener la información del Pokémon {pokemon_name.capitalize()}.")


#Function pokemon abilities

def pokemon_abilities(pokemon_name):
    url_poke_abilities = f"{BASE_URL}/pokemon/{pokemon_name.lower()}"
    response = req.get(url_poke_abilities, verify=False)

    if response.status_code == 200:
        abilities_details = response.json()
        abilities = abilities_details["abilities"]
        
        print(f" {pokemon_name.capitalize()} abilities:")
        for ability in abilities:
            ability_name = ability["ability"]["name"]
            print(f"- {ability_name}")


#Function of pokemon height

def pokemon_height(pokemon_name):
    url_poke_height = f"{BASE_URL}/pokemon/{pokemon_name.lower()}"
    height_response = req.get(url_poke_height, verify=False)

    if height_response.status_code == 200:
        height_details = height_response.json()
        height_decimeters = height_details["height"]
        height = height_decimeters / 10  # Convert decimeters to meters
        print(f"The height of {pokemon_name.capitalize()} is: {height} meters.")
    else:
        print(f"No se pudo obtener la información del Pokémon {pokemon_name.capitalize()}.")



#Function for pokemon weight

def pokemon_weight(pokemon_name):
    url_poke_weight = f"{BASE_URL}/pokemon/{pokemon_name.lower()}"
    weight_response = req.get(url_poke_weight, verify=False)

    if weight_response.status_code == 200:
        weight_details = weight_response.json()
        weight_hectograms = weight_details["weight"]
        weight = int(weight_hectograms / 10) # Convert hectograms to kilograms
        print(f"The weight of {pokemon_name.capitalize()} is : {weight} kilograms")

pokemon_abilities(pokemon_name="charmander")

import requests

def get_pokemon_by_generation(generation):
    url = f"https://pokeapi.co/api/v2/generation/{generation}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        pokemon_list = data["pokemon_species"]

        print(f"Listado de Pokémon en la generación {generation}:")
        for pokemon in pokemon_list:
            print(pokemon["name"])
    else:
        print(f"Error al obtener datos de la generación {generation}. Código de estado: {response.status_code}")


generation_number = 1
get_pokemon_by_generation(generation_number)

def get_pokemon_image_url(pokemon_name):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        image_url = data["sprites"]["front_default"]

        if image_url:
            return image_url
        else:
            return f"El Pokémon {pokemon_name} no tiene una imagen disponible."
    else:
        return f"Error al obtener datos del Pokémon {pokemon_name}. Código de estado: {response.status_code}"



