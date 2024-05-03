## Examen Parcial de Taller de Lenguaje de Programación 3 - Python para Ciencia de Datos

## Parte Práctica

### Ejercico de Algoritmia

El archivo algoritmia2.py se ejecuta mediante con la opción incorporada de VSC "Ejecutar Archivo de Python" o por el comando:
```bash
py .\algoritmia2.py
```
Luego se ingresa la palabra que desea capitalizar.


## Para ejercicios:

El programa utiliza las bibliotecas `pandas` y `matplotlib`. 

## Dependencias

Para instalar las dependencias necesarias, se ejecuta el siguiente comando en la terminal:

```bash
pip install pandas matplotlib
```

***
## Ejecución del Proyecto
***

```bash
python create-csv-file.py
```

El programa comienza leyendo un archivo CSV ubicado en "data_base" que contiene información sobre las provincias argentinas y sus respectivas localidades utilizando pandas.

Luego, se establece una conexión con la base de datos utilizando sqlalchemy.

Los datos del archivo CSV se insertan en una tabla de la base de datos, mediante la utilización de MySQLdb.

Una vez que los datos se han importado a la base de datos, el programa realiza una serie de operaciones de manipulación de datos, incluyendo la agrupación de localidades por provincia.

Finalmente, cada grupo de localidades se exporta a un archivo con el nombre de cada provincia dentro del directorio csv_province.