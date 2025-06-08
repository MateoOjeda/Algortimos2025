# 2.Eliminar de una pila todos los elementos impares, es decir que en la misma solo queden números pares.
from random import randint
from ClasesPilas import Stack

elemt_pila = Stack()
pila_par = Stack()

for i in range(5):
    rand_number = randint(1, 100)
    elemt_pila.push(rand_number)

print("- Pila Generada: ")
elemt_pila.show() # mostramos los elementos de la pila   

# Ahora vemos si el numero es par -----------------
while elemt_pila.size() > 0:
    numero = elemt_pila.pop()
    if ((numero % 2 ) == 0): 
        pila_par.push(numero)

print("- Pila con los valores par: ")
pila_par.show()