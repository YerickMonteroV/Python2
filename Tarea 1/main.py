#importar las funciones 
from poke2 import *


#variable para guardar la opcion seleccionada


#Ciclo para mostar el menu de opciones
while True:
    print("Bienvenidos al Pokedex de Papo")
    
    print("Para datos sobre un pokemon especifico")
    print("opcion 1-Tipo de Pokemon")
    print("Opcion 2-Estus del Pokemon(Vida,Ataque,Defensa)")
    print("opcion 3-Abilidades del Pokemon")
    print("opcion 4-Peso del Pokemon")
    print("opcion 5-Altura del Pokemon")
    print("Para salir digite:0")
    pok=input("Digite el nombre del Pokemon:")
    opcion=input("Digite la opcion:")
    if opcion=="1":
      print(f"{pok.capitalize()} es un pokemon de tipo:")
      print(pokemon_type(pok))
      
   # if opcion=="2":
      #result=Categojoke()
      #esta variable guarda la categoria selecionada por el usuario
      # para poder utilizar la funcion Selecjoke
     # cat=input("Digite la categoria de preferencia:")
     # result=Selecjoke(cat)
 



