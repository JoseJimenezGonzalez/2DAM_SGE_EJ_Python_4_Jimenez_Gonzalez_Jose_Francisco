#Ej7.
#Crear una función que tome una lista de números y devuelva el factorial de esos numeros, se suma el total. Reduce()
from functools import reduce
lista_numeros = [1, 2, 3, 4] #Factorial = 1 + 2 + 6 + 24 = 33

def operacion(acumulador, numero):
    factorial = 1
    for i in range(2, numero + 1):
        factorial *= i
    return acumulador + factorial

print(reduce(operacion, lista_numeros))