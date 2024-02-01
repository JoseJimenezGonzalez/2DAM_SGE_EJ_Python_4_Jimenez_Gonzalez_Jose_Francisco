#Filtrar las palabras que tengan tres o más letras de una lista:
#Lo he puesto mayor que 3 para comprobarlo porque sino no filtraria nada
#asi no sale la palabra paz que tiene len 3

palabras = ["amor", "paz", "guerra", "dolor", "felicidad"]

def obtener_palabra_longitud(palabra):
    return len(palabra) > 3

# Debes pasar la función de filtrado y la lista como argumentos a la función filter
lista_resultante = list(filter(obtener_palabra_longitud, palabras))

print(lista_resultante)
