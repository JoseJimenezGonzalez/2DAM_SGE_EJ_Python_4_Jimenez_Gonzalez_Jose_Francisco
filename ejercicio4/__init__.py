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

    for fila in lector_csv:
        nombre_juego = fila['Juego']
        lista_juegos.append({nombre_juego: fila})

# Mostrar la lista resultante
print(lista_juegos)
