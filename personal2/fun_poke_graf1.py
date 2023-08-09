import requests as req
import matplotlib.pyplot as plt

PokeApi = "https://pokeapi.co/api/v2"

def est_pokemon(pokemon_name):
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
            print(f"- {stat_name}: {stat_value}")

        # Crear el gráfico de barras verticales
        plt.bar(stat_names, stat_values)
        plt.xlabel('Estadísticas')
        plt.ylabel('Valores')
        plt.title(f'Estadísticas de {pokemon_name}')
        plt.xticks(rotation=45)  # Rotar etiquetas para mayor legibilidad

        # Mostrar el gráfico
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
        return None

def peso_pokemon(pokemon_name):
    url_peso = f"{PokeApi}/pokemon/{pokemon_name.lower()}"
    response = req.get(url_peso, verify=False)

    if response.status_code == 200:
        pesos = response.json()
        peso_poke = pesos["weight"]
        return peso_poke
    else:
        print("Error")
        return None

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
plot_altura_peso("pikachu")
