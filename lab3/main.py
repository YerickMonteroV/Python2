#importar las funciones 
from joke import *


#variable para guardar la opcion seleccionada
opcion=""
#Ciclo para mostar el menu de opciones
while opcion!="0":
    print("Chistes de Chuck Norris")
    print("Para seleccionar un chiste al azar digite: 1")
    print("Para seleccionar un chiste por categoria digite:2")
    print("Para salir digite:0")
    opcion=input("Digite la operacion a realizar:")
    #dependiendo de la opcion seleccionada se llama 
    # la funcion correspondiente
    result=0
    if opcion=="1":
      result=Ramdonjoke()
    if opcion=="2":
      result=Categojoke()
      #esta variable guarda la categoria selecionada por el usuario
      # para poder utilizar la funcion Selecjoke
      cat=input("Digite la categoria de preferencia:")
      result=Selecjoke(cat)
 
    

    

 



