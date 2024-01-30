# Ej8.
# Partiendo del siguiente diccionario, crea 2 diccionarios por separado uno con los aprobados y sus notas, y otro para los suspensos.
import csv

notas = {
    "Carmen": 5,
    "Antonio": 4,
    "Juan": 8,
    "Mónica": 9,
    "María": 6,
    "Pablo": 3,
    "Pedro": 7,
    "Ana": 10,
    "Luis": 2,
    "Julia": 1,
    "Jorge": 6,
    "Daniel": 9,
    "Elena": 5,
}
# Filtrar aprobados y almacenar en el diccionario 'aprobados'
aprobados = {nombre: nota for nombre, nota in notas.items() if nota >= 5}

# Filtrar suspendidos y almacenar en el diccionario 'suspendidos'
suspendidos = {nombre: nota for nombre, nota in notas.items() if nota < 5}

print("Aprobados:", aprobados)
print("Suspendidos:", suspendidos)

#Ejercicio 9 Crea 2 archivos csv para el ejercicio anterior.

# Escribir el diccionario de aprobados en un archivo CSV
with open('aprobados.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Nombre', 'Nota'])  # Escribir encabezados
    for nombre, nota in aprobados.items():
        writer.writerow([nombre, nota])

# Escribir el diccionario de suspendidos en un archivo CSV
with open('suspendidos.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Nombre', 'Nota'])  # Escribir encabezados
    for nombre, nota in suspendidos.items():
        writer.writerow([nombre, nota])
