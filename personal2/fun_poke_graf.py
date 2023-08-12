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


