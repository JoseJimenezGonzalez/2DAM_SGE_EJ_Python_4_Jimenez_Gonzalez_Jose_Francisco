#Ej7.
#Crear una función que tome una lista de números y devuelva el factorial de ese número. Reduce()
from functools import reduce
lista_numeros = [1, 2, 3, 4]

def factorial(numero):
    factorial = 1
    for i in range(2, numero + 1):
        factorial *= i
    return factorial

print(list(reduce(factorial, 1,lista_numeros)))