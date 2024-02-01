
def funcion_principal(opcion):
    lista = [4, 8, 14, 22]
    if opcion == "mostrar":
        resultado = lista
    elif opcion == "modificar":
        resultado = [int(elemento) * 2 for elemento in lista]
    elif opcion == "longitud":
        resultado = "La lista tiene " + str(len(lista)) + " elementos."
    else:
        resultado = "No se reconoce esa opcion"
    print(resultado)


print("¿Quieres mostrar, modificar o longitud?")
opcion = input()

funcion_principal(opcion)