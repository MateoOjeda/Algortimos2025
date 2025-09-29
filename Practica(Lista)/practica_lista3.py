# 3.Dada una lista de números enteros, implementar un algoritmo para dividir dicha lista en dos, 
#   una que contenga los números pares y otra para los números impares.

from ClaseLista import List

lista_numeros = List()

numeros = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

for numero in numeros:
    lista_numeros.append(numero)

print("- Lista de numeros: ")
lista_numeros.show()

lista_pares = List()
lista_impares = List()

for numero in lista_numeros:
    if numero % 2 == 0:
        lista_pares.append(numero)
    else:
        lista_impares.append(numero)

print("- Lista de numeros pares:")
lista_pares.show()
print("----------------------------")
print("- Lista de numero impares:")
lista_impares.show()