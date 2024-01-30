#Ej5.
#Partiendo del fichero CSV llamado juegos.csv:
#Trasladarlo a un diccionario de diccionarios donde la clave del diccionario principal sea el nombre del juego.

import csv

# Nombre del archivo CSV
archivo_csv = "juegos.csv"

# Diccionario para almacenar los juegos
diccionario_juegos = {}

# Abrir el archivo CSV y leer su contenido
with open(archivo_csv, mode='r') as file:
    # Crear un objeto lector de CSV
    lector_csv = csv.DictReader(file, delimiter=";")

    # Iterar sobre las filas del CSV y agregar al diccionario
    for fila in lector_csv:
        # Utilizar el nombre del juego como clave y almacenar el diccionario correspondiente
        diccionario_juegos[fila['Juego']] = {
            'Juego': fila['Juego'],
            'Precio': fila['Precio'],
            'Genero': fila['Genero']  # Convertir el año a entero si es necesario
        }

# Mostrar el diccionario resultante
print(diccionario_juegos)

archivo_csv_destino = "juegos2.csv"

# Guardar el diccionario en un nuevo archivo CSV
with open(archivo_csv_destino, mode='w', newline='') as file:
    # Definir los encabezados
    encabezados = ['Juego', 'Precio', 'Genero']

    # Crear un escritor de CSV
    escritor_csv = csv.DictWriter(file, fieldnames=encabezados)

    # Escribir los encabezados en el archivo
    escritor_csv.writeheader()

    # Escribir las filas en el archivo
    for nombre, juego_info in diccionario_juegos.items():
        escritor_csv.writerow({'Juego': nombre, 'Precio': juego_info['Precio'], 'Genero': juego_info['Genero']})

print(f"El archivo '{archivo_csv_destino}' ha sido creado con éxito.")
