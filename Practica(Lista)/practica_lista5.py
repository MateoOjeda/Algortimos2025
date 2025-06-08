# 5.Dada una lista de números enteros eliminar de estas los números primos.

from ClaseLista import List
from random import randint

lista_numeros = List()


for numeros in range(20):
    lista_numeros.append(randint(1,30))

print("- Lista de numeros: ")
lista_numeros.show()

# eliminar los numero primos
for numero in lista_numeros.copy():
    if numero < 2:
        continue
    es_primo = True
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            es_primo = False
            break
    if es_primo:
        lista_numeros.remove(numero)

print("- Lista de numeros sin primos: ")
lista_numeros.show()