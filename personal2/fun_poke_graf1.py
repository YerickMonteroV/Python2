import requests as req
import matplotlib.pyplot as plt
import pandas as pd

PokeApi = "https://pokeapi.co/api/v2"

def est_pokemon_graf(pokemon_name):
    urlestatus = f"{PokeApi}/pokemon/{pokemon_name.lower()}"
    response = req.get(urlestatus, verify=False)

    if response.status_code == 200:
        datapoke = response.json()
        datos = datapoke["stats"]

        stat_names = []
        stat_values = []

        for stat in datos:
            stat_name = stat["stat"]["name"]
            stat_value = stat["base_stat"]
            stat_names.append(stat_name)
            stat_values.append(stat_value)
            #print(f"- {stat_name}: {stat_value}")

         # Crear el gráfico de pie
        plt.pie(stat_values, labels=stat_names, autopct='%1.1f%%', startangle=140)
        plt.axis('equal')  # Hace que el gráfico de pie se vea como un círculo

        plt.title(f'Estadísticas de {pokemon_name}')
        #mostrar grafico
        plt.tight_layout()  # Ajustar diseño
        plt.show()
    else:
        print("Error")

# Llamada a la función con el nombre de un Pokémon
def poke_altura(pokemon_name):
    url_altura = f"{PokeApi}/pokemon/{pokemon_name.lower()}"
    response = req.get(url_altura, verify=False)

    if response.status_code == 200:
        alturas = response.json()
        altu_poke = alturas["height"]
        return altu_poke
    else:
        print("Error")
        

def peso_pokemon(pokemon_name):
    url_peso = f"{PokeApi}/pokemon/{pokemon_name.lower()}"
    response = req.get(url_peso, verify=False)

    if response.status_code == 200:
        pesos = response.json()
        peso_poke = pesos["weight"]
        return peso_poke
    else:
        print("Error")
        

def plot_altura_peso(pokemon_name):

    altura = poke_altura(pokemon_name)
    peso = peso_pokemon(pokemon_name)

    if altura is not None and peso is not None:
       datos = [altura, peso]
       etiquetas = ['Altura', 'Peso']
        
       plt.bar(etiquetas, datos, color=['blue', 'green'])
       plt.xlabel('Medida')
       plt.ylabel('Valor')
       plt.title(f'Altura y Peso de {pokemon_name.capitalize()}')
       plt.show()

    # Llamada a la función para crear el gráfico


def tipo_pokemon(pokemon_name):
    urltipo_poke = f"{PokeApi}/pokemon/{pokemon_name.lower()}"
    response = req.get(urltipo_poke, verify=False)

    if response.status_code == 200:
        datapoke = response.json()
        tipos = datapoke["types"]
        tipo_poke_list = [tipo["type"]["name"] for tipo in tipos]
        return tipo_poke_list
    else:
        return []

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

def est_pokemon_graf(pokemon_name):
    
   # Obtener los tipos y habilidades del Pokemon
   tipos = tipo_pokemon(pokemon_name)
   habilidades = habil_pokemon(pokemon_name)

# Crear un DataFrame de Pandas
   data = {
    "Tipo": tipos,
    "Habilidades": habilidades
     }
   df = pd.DataFrame(data)

# Mostrar el DataFrame
   print(df)

# Ejecutar la función para mostrar el gráfico de estadísticas
est_pokemon_graf("pikachu")