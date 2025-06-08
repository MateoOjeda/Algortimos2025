# 11. Dada una pila de letras determinar cuántas vocales contiene.

from ClasesPilas import Stack

elem_pila = Stack() # creo la pila
cantidad_vocales = 0

def contador_voc(pila):
    vocales = "aeiouAEIOU"
    cont_voc = 0
    pila_aux = Stack()

    while pila.size() > 0: # recorro la pila (original)
       letra = pila.pop()

       if letra in vocales:
        cont_voc += 1
        
        pila_aux.push(letra)
       
    while pila_aux.size() > 0:
        pila.push(pila_aux.pop())

    return cont_voc

letras = ['a', 'b', 'c', 'e', 'i', 'o', 'u', 'x']

for letra in letras:
    elem_pila.push(letra)

print("- Pila de letras: ")
elem_pila.show()

cantidad_vocales = contador_voc(elem_pila)
print("- Cantidad de vocales: ", cantidad_vocales)