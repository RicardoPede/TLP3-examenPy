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
def calcular_valor_inventario(productos):
    for producto in productos:
        producto['valor_inventario'] = producto['precio'] * producto['cantidad_disponible']
    return productos

print("con valor inventario: ", calcular_valor_inventario(productos))

# Punto 2
def calcular_valor_total_inventario(productos):
    return sum(producto['valor_inventario'] for producto in productos)

valor_inventario = calcular_valor_inventario(productos)
print("Valor total del inventario: ", calcular_valor_total_inventario(valor_inventario))

# Punto 3
ventas = [
    {'nombre': 'Camiseta', 'cantidad_vendida': 5},
]

def simular_ventas(productos, ventas):
    for venta in ventas:
        for producto in productos:
            if producto['nombre'] == venta['nombre']:
                producto['cantidad_disponible'] -= venta['cantidad_vendida']
    return productos
    
simulacro_venta = simular_ventas(productos, ventas)

# Punto 4
print(simulacro_venta)


# Punto 5
def crear_dataframe(productos):
    df = pd.DataFrame(productos)
    return df[['nombre', 'cantidad_disponible']]

df = crear_dataframe(productos)