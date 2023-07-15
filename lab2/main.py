#importe todas las galerias que necesitaba.
from api import *
from ids import elem
import time
#cree una variable que se igualara a lista externa.
usuarios = elem
#cree una variable para guardar el tiempo de inicio.
tiempo=time.time()
#corri un ciclo donde pregunte por cada uno de los usuarios que viene en la lista.
for user in usuarios:
    #Guarde la info en una variable y la imprimimos.
    resultado = getOneUser(user)
    print(resultado)
#otra variable para hacer la medicion del tiempo de espera, restandole al tiempo actual el tiempo inicial de la funcion y al final imprimo el tiempo.
espera=time.time()-tiempo
print(espera)


