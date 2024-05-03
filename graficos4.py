from pandas3 import df
import matplotlib.pyplot as plt 

def grafico_barras(df): # grafica un gráfico de barras con los productos y la cantidad disponible
    plt.figure(figsize=(10, 6)) # tamaño de la figura
    plt.bar(df['nombre'], df['cantidad_disponible']) # gráfico de barras
    plt.xticks(df['nombre'], rotation='vertical') # etiquetas en el eje x
    plt.ylabel('Cantidad disponible') # etiqueta en el eje y
    plt.title('My first Grafic :) ("Cantidad de Productos")') # título del gráfico
    plt.grid(True) # cuadrícula
    plt.show() # muestra el gráfico

grafico_barras(df) 