# 4.Invertir el contenido de una pila, solo puede utilizar una pila auxiliar como estructura extra.

from random import randint
from ClasesPilas import Stack

elem_pila = Stack() # creo la pila

for i in range(5): # la lleno de numero random del 1 al 100
    rand_number = randint(1, 100)
    elem_pila.push(rand_number)

print("- Pila Generada: ")
elem_pila.show() # mostramos los elementos de la pila 

pila_aux = Stack() # creo la pila auxiliar

while elem_pila.size() > 0: # mientras la pila no este vacia
    pila_aux.push(elem_pila.pop()) # voy sacando los elementos de la pila original y los voy metiendo en la auxiliar

while pila_aux.size() > 0:
    elem_pila.push(pila_aux.pop())

print("- Pila Invertida:")
while elem_pila.size() > 0:
    print(elem_pila.pop())

#preguntarle al profesor.



















