# 9. Resolver el problema del factorial de un número utilizando una pila.

from ClasesPilas import Stack

numeros_pila = Stack()
ing_num = int (input("- Ingrese un numero para calcular su factorial: !"))

factorial = 1 # inicializamos el factorial en 1

for i in range(1,ing_num + 1):
    numeros_pila.push(i)
    numero_calculado = numeros_pila.pop() # sacamos el elemento de la pila
    factorial = numero_calculado * factorial

print("- Pila Generada: ")
numeros_pila.show() # mostramos los elementos de la pila   

print("- Factorial: ", factorial) # mostramos el factorial
print("- Factorial de ", ing_num, " es: ", factorial) # mostramos el factorial