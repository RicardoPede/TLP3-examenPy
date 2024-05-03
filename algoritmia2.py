# Se está trabajando en un programa que necesita capitalizar 
# palabras, pero el desafío es que solo la primera letra 
# debe ser convertida a mayúscula, manteniendo las demás
# letras sin cambios.

palabra = str(input("Ingrese su nombre:")) # se ingresa el nombre o nombres

def capitalizar_cadena(cadena): # función que capitaliza la cadena
    palabras = cadena.split() # divide la cadena en palabras
    palabras_capitalizadas = [capitalizar_palabra(palabra) for palabra in palabras] # capitaliza cada palabra
    return ' '.join(palabras_capitalizadas) # une las palabras capitalizadas en una cadena

def capitalizar_palabra(palabra): # función que capitaliza la palabra
    if len(palabra) > 0: # si la palabra tiene más de 0 caracteres
        return palabra[0].upper() + palabra[1:] # convierte la primera letra en mayúscula y mantiene las demás letras sin cambios
    else:
        return palabra # si la palabra no tiene caracteres, devuelve la palabra sin cambios
    
print(capitalizar_cadena(palabra)) # imprime la cadena capitalizada

# ejemplo: Ingrese su nombre: ricardo martin pedemonte
# respuesta: Ricardo Martin Pedemonte