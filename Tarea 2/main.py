#importamos las funciones 
from fun_poke_graf import *

print("Bienvenidos al Pokedex de Papo")
#variable para guardar la opcion seleccionada
pok=input("Digite el nombre del Pokemon que deseas buscar:")
opcion=""
#Ciclo para mostar el menu de opciones las veces necesarias hasta que
#el usuario desee salir
#actualize el menu con las nuevas funciones
while opcion!="0":
    print("opcion 1-Tipo de Pokemon")
    print("Opcion 2-Estus del Pokemon(Vida,Ataque,Defensa)")
    print("opcion 3-Abilidades del Pokemon")
    print("opcion 4-Peso y Altura del Pokemon")
    print("opcion 5-Para ver una imagen del Pokemon")
    print("opcion 6-Para cambiar el Pokemon seleccionado")
    print("opcion 7-Para ver todos los pokemones segun la generacion seleccionada(1-9)")
    print("Para salir digite:0")
#Despues de mostrar el menu, actualizamos la variable opcion con los
#datos ingresados por el usuario y corremos la funciones de acuerdo a la opcion seleccionada.
    opcion=input("Digite la opcion:")
    if opcion=="1":
      print(f"{pok.capitalize()} es un pokemon de tipo:")
      print(tipo_pokemon(pok))
    elif opcion=="2":
       print(f"El estatus de {pok.capitalize()} es:")
       print(est_pokemon(pok))
    elif opcion=="3":
       print(habil_pokemon(pok))
    elif opcion=="4":
       print(f"El peso y la altura de {pok.capitalize()} es:")
       print(graf_altura_peso(pok))
    elif opcion=="5":
       print(f"Abra el link para ver una imagen de {pok.capitalize()}")
       print(imag_poke(pok))
    elif opcion=="6":
       pok=input("Digite el nombre del nuevoPokemon que deseas buscar:")
    elif opcion=="7":
       x=input("Digite la generacion")
       gen_pokemon(x)