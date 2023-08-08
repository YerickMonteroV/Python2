#Importe las galerias necesarias.
import pandas as pd
import matplotlib.pyplot as plt
#Hice una variable con la documento que tiene la informacion.
info="ventas.csv"
#Con la funciones de pandas leemos el documento y lo imprimimos.
dataFrame=pd.read_csv(info)
print(dataFrame)
#Creo un dataframe con las ganancion, ventas-gastos.
dataFrame["Ganancias"]= dataFrame["Ventas"]-dataFrame["Gastos"]
print(dataFrame)
#Cree variable con las info de cada linea.
meses = dataFrame["Mes"]
ventas = dataFrame["Ventas"]
gastos = dataFrame["Gastos"]
#Escogemos el diseño y las barras que vamos a utilizar
mes = range(len(meses))
plt.figure(figsize=(15, 6)) 
plt.bar(mes, ventas, color='blue', width=0.4)
plt.bar([i + 0.4 for i in mes], gastos, color='orange', width=0.4)
plt.xticks([i + 0.2 for i in mes], meses)

# Escribimos el titulo del grafico,la etiquetas de cada eje y la leyenda.
plt.title("Grafica de evolución mensual de ventas y gastos")
plt.xlabel("Meses")
plt.ylabel("Cantidad")
plt.legend(labels=['Ventas', 'Gastos'], loc='upper left')
# Finalmente mostramos el gráfico
plt.show()