# 1. Desarrollar un algoritmo que permita cargar 1000 número enteros –generados de manera aleatoria–
# que resuelva las siguientes actividades:

from random import randint
from ClaseArbol import BinaryTree

#cargo el arbol con 1000 numeros aleatorios
arbol = BinaryTree()

for _ in range(10):
    num = randint(1,10)
    arbol.insert(num)

# a. realizar los barridos preorden, inorden, postorden y por nivel sobre el árbol generado;
print("Punto a--------------")
print("barrido preorden:")
arbol.pre_order()
print("\nbarrido inorden:")
arbol.in_order()
print("\nbarrido postorden:")
arbol.post_order()
print("\nbarrido por nivel:")
arbol.by_level()

# b. determinar si un número está cargado en el árbol o no;
print("Punto b--------------")
numero_ingresado = int(input("Igrese un numero para buscarlo en el arbol: "))

if arbol.search(numero_ingresado):
    print("el numero se encuentra en el arbol")
else:
    print("no se encontro el numero")

# c. eliminar tres valores del árbol;
print("Punto c--------------")
numero_1 = int(input("Igrese un numero(1) para eliminar del arbol: "))
numero_2 = int(input("Igrese un numero(2) para eliminar del arbol: "))
numero_3 = int(input("Igrese un numero(3) para eliminar del arbol: "))

arbol.delete(numero_1)
arbol.delete(numero_2)      
arbol.delete(numero_3)
# muestro el arbol con los valores eliminados
arbol.by_level()

# d. determinar la altura del subárbol izquierdo y del subárbol derecho;
print("Punto d--------------")
if arbol.root is not None:
    altura_izq = arbol.height(arbol.root.left)
    altura_der = arbol.height(arbol.root.right)
    print(f"Altura del subarbol izquierdo: {altura_izq}")
    print(f"Altura del subarbol derecho: {altura_der}")
else:
    print("el Arbol esta vacio")


# e. determinar la cantidad de ocurrencias de un elemento en el árbol;
print("Punto e--------------")
def contar_ocurrencias(root, valor):
    if root is None:
        return 0
    count = 1 if root.value == valor else 0
    return count + contar_ocurrencias(root.left, valor) + contar_ocurrencias(root.right, valor)

numero = int(input("Ingrese un numero para contar: "))
ocurrencias = contar_ocurrencias(arbol.root, numero)

print(f"El número {numero} aparece {ocurrencias} veces en el árbol.")

# f. contar cuántos números pares e impares hay en el árbol.
print("Punto f--------------")
def contar_pares_impares(root):
    if root is None:
        return (0, 0)
    pares_izq, impares_izq = contar_pares_impares(root.left)
    pares_der, impares_der = contar_pares_impares(root.right)
    if root.value % 2 == 0:
        pares = 1 + pares_izq + pares_der
        impares = impares_izq + impares_der
    else:
        impares = 1 + impares_izq + impares_der
        pares = pares_izq + pares_der
    return pares, impares

pares, impares = contar_pares_impares(arbol.root)
print(f"Números pares: {pares}")
print(f"Números impares: {impares}")


