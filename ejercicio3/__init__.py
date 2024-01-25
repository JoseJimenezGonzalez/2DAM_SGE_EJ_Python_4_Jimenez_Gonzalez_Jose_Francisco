#Filtrar las palabras que tengan tres o más letras de una lista:

palabras = ["amor", "paz", "guerra", "dolor", "felicidad"]

def obtener_palabra_longitud(palabra):
    return len(palabra) > 3

# Debes pasar la función de filtrado y la lista como argumentos a la función filter
lista_resultante = list(filter(obtener_palabra_longitud, palabras))

print(lista_resultante)
