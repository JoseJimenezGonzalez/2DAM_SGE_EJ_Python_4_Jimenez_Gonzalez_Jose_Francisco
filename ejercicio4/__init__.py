#Partiendo del fichero CSV llamado juegos.csv:
#Leer su contenido y trasladarlo una estructura Python tipo lista de diccionarios.

import csv

# Nombre del archivo CSV
archivo_csv = "juegos.csv"

# Lista para almacenar los diccionarios
lista_juegos = []

# Abrir el archivo CSV y leer su contenido
with open(archivo_csv, mode='r') as file:
    # Crear un objeto lector de CSV
    lector_csv = csv.DictReader(file, delimiter=";")

    # Iterar sobre las filas del CSV y agregar a la lista de diccionarios
    for fila in lector_csv:
        lista_juegos.append(fila)

# Mostrar la lista resultante
print(lista_juegos)
