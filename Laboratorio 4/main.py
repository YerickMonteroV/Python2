import pandas as pd
import matplotlib.pyplot as plt
info="ventas.csv"

dataFrame=pd.read_csv(info)
print(dataFrame)

dataFrame["Ganancias"]= dataFrame["Ventas"]-dataFrame["Gastos"]
print(dataFrame)

meses = dataFrame["Mes"]
ventas = dataFrame["Ventas"]
gastos = dataFrame["Gastos"]

x = range(len(meses))
plt.figure(figsize=(10, 6))  # Tamaño de la figura
plt.bar(x, ventas, label="Ventas", color='blue', width=0.4)
plt.bar([i + 0.4 for i in x], gastos, label="Gastos", color='red', width=0.4)

# Configurar los ticks del eje x
plt.xticks([i + 0.2 for i in x], meses)

# Etiquetas y título
plt.xlabel("Mes")
plt.ylabel("Cantidad")
plt.title("Evolución mensual de ventas y gastos")
plt.legend()  # Agregar leyenda

# Mostrar el gráfico
plt.grid(True)  # Agregar una cuadrícula al gráfico
plt.show()