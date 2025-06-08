# 14. Realizar un algoritmo que permita ingresar elementos en una pila, y que estos queden ordenados
# de forma creciente. Solo puede utilizar una pila auxiliar como estructura extra (no se
# pueden utilizar métodos de ordenamiento).

from ClasesPilas import Stack

elem_pila = Stack()

for i in range(5):
    numero = int(input("- Ingrese un numero: "))
    elem_pila.push(numero)

print("- Pila Inicial:")
elem_pila.show()

pila_aux = Stack()

while elem_pila.size() > 0:
    valores = elem_pila.pop()

    while pila_aux.size() > 0 and valores < pila_aux.on_top():
        elem_pila.push(pila_aux.pop())
    pila_aux.push(valores)

while pila_aux.size() > 0:
    elem_pila.push(pila_aux.pop())

print("- Pila Ordenada:")
elem_pila.show()
