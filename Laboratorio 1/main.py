from Trig import *
import os
persona=Trig()
opcion="0"

while opcion!="Salir":
    print("Para calcular seno de π digite: seno")
    print("Para calcular coseno de π digite: coseno")
    print("Para calcular tangente de π digite: tangente")
    print("Para salir digite:Salir")
    opcion=input("Digite la operacion a realizar:")
    result=0
    if opcion=="seno":
      result=persona.seno()
      print(f"El seno de π es: {result}")
    if opcion=="coseno":
          result=persona.coseno()
          print(f"El coseno de π es: {result}")
    else:
          if opcion=="tangente":
            result=persona.tangente()
            print(f"El tangente de π es: {result}")
    with open("log.txt","a") as file:
      file.write(f"El resultado del {opcion} es {result} y fue realizada en {persona.dat()}\n")