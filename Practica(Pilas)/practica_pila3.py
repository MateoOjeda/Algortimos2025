# 3.Reemplazar todas las ocurrencias de un determinado elemento en una pila.

from random import randint
from ClasesPilas import Stack

elemento_pila = Stack()

for i in range(5):
    rand_number = randint(1, 100)
    elemento_pila.push(rand_number)

print("- Pila Generada: ")
elemento_pila.show() # mostramos los elementos de la pila   

numero_ing = int (input("- Ingrese un numero: "))

pila_aux = Stack()  

while elemento_pila.size() > 0:
    numero = elemento_pila.pop()
    if numero == numero_ing: 
        pila_aux.push(0)
    else:
        pila_aux.push(numero)
    
    
while pila_aux.size() > 0:
    elemento_pila.push(pila_aux.pop())

print("- Pila Generada(con el valor cambiado): ")
elemento_pila.show()