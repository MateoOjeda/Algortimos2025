# 1. Determinar el número de ocurrencias de un determinado elemento en una pila.

from random import randint

from ClasesPilas import Stack # Aca estoy importando las clase pila desde otro programa.
 
elem_pila = Stack()

for i in range(5):
    rand_number = randint(1, 100)
    elem_pila.push(rand_number)

print("- Pila Generada: ")
elem_pila.show() # mostramos los elementos de la pila   

# ! nota importante: hacer la declaracion de variables asi.

numero_ing = int (input("- Ingrese un numero: ")) #ingresamos el valor que deseamos contar

cant_pila = Stack()
contador = 0

# Ahora contamos la cantidad de veces que se repite -----------------
while elem_pila.size() > 0:
    numero = elem_pila.pop()
    if numero == numero_ing: 
        contador += 1
    cant_pila.push(numero) # guardo el valor para que no se pierda en la pila

# Restauro la pila
while cant_pila.size() > 0:
    elem_pila.push(cant_pila.pop())
print("Cantidad de veces que se repite el digito: " , contador)

