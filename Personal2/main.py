#importar las funciones 
from poke2 import *


#variable para guardar la opcion seleccionada
#Ciclo para mostar el menu de opciones
print("Bienvenidos al Pokedex de Papo")
pok=input("Digite el nombre del Pokemon que deseas buscar:")
opcion=""
while opcion!="0":
    
    
    
    print("opcion 1-Tipo de Pokemon")
    print("Opcion 2-Estus del Pokemon(Vida,Ataque,Defensa)")
    print("opcion 3-Abilidades del Pokemon")
    print("opcion 4-Peso del Pokemon")
    print("opcion 5-Altura del Pokemon")
    print("opcion 6-Para ver una imagen del Pokemon")
    print("opcion 7-Para cambiar el Pokemon seleccionado")
    print("opcion 8-Para cambiar el Pokemon seleccionado")
    print("Para salir digite:0")
    
    opcion=input("Digite la opcion:")
    if opcion=="1":
      print(f"{pok.capitalize()} es un pokemon de tipo:")
      print(tipo_pokemon(pok))
    elif opcion=="2":
       print(f"El estatus de {pok.capitalize()} es:")
       print(est_pokemon(pok))
    elif opcion=="3":
       print(f"Las abilidades de {pok.capitalize()} son:")
       print(habil_pokemon(pok))
    elif opcion=="4":
       print(f"El peso de {pok.capitalize()} es:")
       print(peso_pokemon(pok))
    elif opcion=="5":
       print(f"La altura de {pok.capitalize()} es:")
       print(alt_pokemon(pok))
    elif opcion=="6":
       print(f"Abra el link para ver una imagen de {pok.capitalize()}")
       print(imag_pokemon(pok))
    elif opcion=="7":
       pok=input("Digite el nombre del nuevoPokemon que deseas buscar:")
    elif opcion=="8":
       x=input("Digite la generacion")
       gen_pokemon(x)

   
       
         
      

 



