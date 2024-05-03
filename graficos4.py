from pandas3 import df
import matplotlib.pyplot as plt

def grafico_barras(df):
    plt.figure(figsize=(10, 6))
    plt.bar(df['nombre'], df['cantidad_disponible'])
    plt.xticks(df['nombre'], rotation='vertical')
    plt.ylabel('Cantidad disponible')
    plt.title('My first Grafic :) ("Cantidad de Productos")')
    plt.grid(True)
    plt.show()

grafico_barras(df)