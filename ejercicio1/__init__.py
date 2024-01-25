#Ejercicio 1

COMIDA_DEFECTO = "No tenemos de ese tipo de comida"

diccionario = {"fruta": "Manzana, platano o pera",
               "verdura": "Tomate, lechuga o zanahoria",
               "carne": "Cerdo, ternera o pollo",
               "Pescado": "Sardinas, caballa o salmonete"}

opcion = input("¿Que tipo de comida quieres?")
eleccion_comida = diccionario.get(opcion.lower(), COMIDA_DEFECTO)
print(f"La eleccion de comida es: {eleccion_comida}")

