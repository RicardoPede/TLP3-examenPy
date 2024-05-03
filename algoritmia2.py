# Se está trabajando en un programa que necesita capitalizar 
# palabras, pero el desafío es que solo la primera letra 
# debe ser convertida a mayúscula, manteniendo las demás
# letras sin cambios.

palabra = str(input("Ingrese su nombre:"))

def capitalizar_cadena(cadena):
    palabras = cadena.split()
    palabras_capitalizadas = [capitalizar_palabra(palabra) for palabra in palabras]
    return ' '.join(palabras_capitalizadas)

def capitalizar_palabra(palabra):
    if len(palabra) > 0:
        return palabra[0].upper() + palabra[1:]
    else:
        return palabra
    
print(capitalizar_cadena(palabra))

# ejemplo: Ingrese su nombre: ricardo martin pedemonte
# respuesta: Ricardo Martin Pedemonte