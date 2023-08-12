import requests as req
import pandas as pd



PokeApi = "https://pokeapi.co/api/v2"

def habil_pokemon(pokemon_name):
    urlHabil = f"{PokeApi}/pokemon/{pokemon_name.lower()}"
    response = req.get(urlHabil, verify=False)

    if response.status_code == 200:
        datapoke = response.json()
        habilidades = datapoke["abilities"]
        
        habilidades_list = [habilidad["ability"]["name"] for habilidad in habilidades]
        return habilidades_list
    else:
        return []

# Nombre del Pokémon que deseas consultar
pokemon_name = "pikachu"

# Obtener la lista de habilidades del Pokémon
habilidades_pokemon = habil_pokemon(pokemon_name)

# Crear un DataFrame de Pandas con los datos
data = {
    "Habilidades": habilidades_pokemon
}
df = pd.DataFrame(data)

# Mostrar el DataFrame
print(df)





