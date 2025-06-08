# Diseñar un algoritmo que elimine todas las vocales que se encuentren en una lista de caracteres.

from ClaseLista import List

lista_vocales = List()

lista_letras = ['e', 'A', 'u', 'd', 'i', 'O', 't', 'a', 'E', 'z']

for letras in lista_letras:
    lista_vocales.append(letras)

print("Mostrar Lista: ")
lista_vocales.show()

vocales = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

for letras in lista_vocales:
    if letras in vocales:
        lista_vocales.delete_value(letras)

print("Eliminar vocales: ")
lista_vocales.show()
