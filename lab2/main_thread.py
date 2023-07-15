#a diferencia del main normal importe la galeria para utilizar tread
from concurrent.futures import ThreadPoolExecutor
from api import *
from ids import elem
import time
#cree una variable que se igualara a lista externa.
usuarios = elem
#cree una variable para guardar el tiempo de inicio.
tiempo = time.time()
#utilize ThreadPoolExecutor
#corri un ciclo donde pregunte por cada uno de los usuarios que viene en la lista.
with ThreadPoolExecutor() as executor:
    resultados = executor.map(getOneUser, usuarios)
    for result in resultados:
        print(result)
#otra variable para hacer la medicion del tiempo de espera, restandole al tiempo actual el tiempo inicial de la funcion y al final imprimo el tiempo.
espera = time.time() - tiempo
print(espera)
