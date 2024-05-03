import pandas as pd

productos = [
    {"nombre": "Camiseta", "precio": 20, "cantidad_disponible": 100},
    {"nombre": "Pantalón", "precio": 30, "cantidad_disponible": 80},
    {"nombre": "Zapatos", "precio": 50, "cantidad_disponible": 50},
    {"nombre": "Reloj", "precio": 100, "cantidad_disponible": 30},
    {"nombre": "Gorra", "precio": 15, "cantidad_disponible": 120},
    {"nombre": "Bufanda", "precio": 25, "cantidad_disponible": 60},
    {"nombre": "Sudadera", "precio": 40, "cantidad_disponible": 70},
    {"nombre": "Bolsa", "precio": 35, "cantidad_disponible": 90},
    {"nombre": "Chaqueta", "precio": 80, "cantidad_disponible": 40},
    {"nombre": "Gafas de sol", "precio": 45, "cantidad_disponible": 25},
    {"nombre": "Calcetines", "precio": 10, "cantidad_disponible": 150},
    {"nombre": "Sombrero", "precio": 20, "cantidad_disponible": 55},
    {"nombre": "Pulsera", "precio": 5, "cantidad_disponible": 200},
    {"nombre": "Pendientes", "precio": 15, "cantidad_disponible": 180},
    {"nombre": "Cinturón", "precio": 20, "cantidad_disponible": 100},
    {"nombre": "Vestido", "precio": 60, "cantidad_disponible": 35},
    {"nombre": "Corbata", "precio": 25, "cantidad_disponible": 75},
    {"nombre": "Bolso", "precio": 70, "cantidad_disponible": 45},
    {"nombre": "Paraguas", "precio": 30, "cantidad_disponible": 65},
    {"nombre": "Collar", "precio": 40, "cantidad_disponible": 85},
]

# Punto 1
def calcular_valor_inventario(productos): # calcula el valor del inventario de cada producto
    for producto in productos: # recorre la lista de productos
        producto['valor_inventario'] = producto['precio'] * producto['cantidad_disponible'] # calcula el valor del inventario
    return productos

print("con valor inventario: ", calcular_valor_inventario(productos))

# Punto 2
def calcular_valor_total_inventario(productos): # calcula el valor total del inventario
    return sum(producto['valor_inventario'] for producto in productos) # suma el valor del inventario de cada producto

valor_inventario = calcular_valor_inventario(productos) # calcula el valor del inventario de cada producto
print("Valor total del inventario: ", calcular_valor_total_inventario(valor_inventario)) # calcula el valor total del inventario

# Punto 3
ventas = [
    {'nombre': 'Camiseta', 'cantidad_vendida': 5},
]

def simular_ventas(productos, ventas): # simula las ventas de los productos
    for venta in ventas: # recorre la lista de ventas
        for producto in productos: # recorre la lista de productos
            if producto['nombre'] == venta['nombre']: # si el nombre del producto es igual al nombre de la venta
                producto['cantidad_disponible'] -= venta['cantidad_vendida'] # resta la cantidad vendida a la cantidad disponible
    return productos
    
simulacro_venta = simular_ventas(productos, ventas) # simula las ventas de los productos

# Punto 4
print(simulacro_venta)


# Punto 5
def crear_dataframe(productos): # crea un dataframe con los productos y la cantidad disponible
    df = pd.DataFrame(productos) # crea un dataframe con los productos
    return df[['nombre', 'cantidad_disponible']] # retorna el dataframe con el nombre y la cantidad disponible

df = crear_dataframe(productos)