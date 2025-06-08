# 7.Eliminar el i-ésimo elemento debajo de la cima de una pila de palabras.

from random import randint
from ClasesPilas import Stack

# creo una funcion que elimine un elemnto de la pila
def eliminar_elem_pila(pila, i):
    pila_aux = Stack()
    pos = 0

    # Sacar elementos de la pila original
    while pila.size() > 0:
        valor = pila.pop()
        if pos == i:
            # Este es el i-ésimo debajo de la cima — lo eliminamos
            pos += 1
            continue
        pila_aux.push(valor)
        pos += 1

    # Restaurar los elementos a la pila original
    while pila_aux.size() > 0:
        pila.push(pila_aux.pop())

# creo y lleno la pila con numero alaeatorios 
elem_pila = Stack() # creo la pila

for i in range(5):
    rand_number = randint(1, 100)
    elem_pila.push(rand_number)

print("- Pila Generada: ")
elem_pila.show() # mostramos los elementos de la pila

i = int(input("Ingrese el índice (0 = cima) del elemento a eliminar: "))
eliminar_elem_pila(elem_pila, i)

print("- Pila después de eliminar:")
elem_pila.show()