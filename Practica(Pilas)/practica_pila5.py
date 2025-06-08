# 5. Determinar si una cadena de caracteres es un palíndromo.

from ClasesPilas import Stack

def palindromo(cadena):
    crea_pila_1 = Stack()
    cadena = ''.join(cadena.split()) # Eliminar espacios en blanco

    #- Apilo la mitad de la cadena
    for char in cadena:
        crea_pila_1.push(char)

    #- Reconstruimos la cadena invertida desde la pila
    cadena_invertida = ''
    while crea_pila_1.size() > 0:
        cadena_invertida += crea_pila_1.pop()

    #- Comparamos la cadena original con la invertida
    return cadena == cadena_invertida

# Ejemplo de uso
cadena = input("Ingrese una cadena de caracteres: ")
if palindromo(cadena):
    print("La cadena es un palíndromo.")
else:
    print("La cadena no es un palíndromo.")
