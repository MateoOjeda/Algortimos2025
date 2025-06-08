# 6. Leer una palabra y visualizarla en forma inversa.

from ClasesPilas import Stack

def inv_palabra(cadena):
    crea_pila = Stack()

    #- Apilo la mitad de la cadena
    for char in cadena:
        crea_pila.push(char)

    #- Reconstruimos la cadena invertida desde la pila
    cadena_invertida = ''

    while crea_pila.size() > 0:
        cadena_invertida += crea_pila.pop()

    #- Comparamos la cadena original con la invertida
    return cadena_invertida

# Ejemplo de uso
cadena = input("Ingrese una palabra de caracteres: ")
cadena_inv = inv_palabra(cadena)
print("la palabra invertida es: ", cadena_inv)