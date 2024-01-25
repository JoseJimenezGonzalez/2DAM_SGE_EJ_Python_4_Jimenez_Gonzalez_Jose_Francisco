print("¿Quieres mostrar, modificar o longitud?")
opcion = input()

def funcion_principal(opcion):
    lista = [4, 8, 14, 22]
    if opcion == "mostrar":
        resultado = lista
    elif opcion == "modificar":
        # Obtener la entrada del usuario como una cadena
        entrada_usuario = input("Introduce los elementos de la lista separados por espacios: ")

        # Dividir la cadena en una lista utilizando el espacio como separador
        lista_resultante = entrada_usuario.split()

        # Puedes convertir los elementos de la lista a tipos de datos específicos si es necesario
        # En este ejemplo, convertimos todos los elementos a enteros
        resultado = [int(elemento) for elemento in lista_resultante]
    else:
        resultado = "La lista tiene" + str(len(lista)) + " elementos."
    print(resultado)
