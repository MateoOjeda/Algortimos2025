# - Resumen de las clases de las pilas.
from typing import Any, Optional
'''
importa herramientas del módulo typing, que se usa para anotar tipos en Python, 
especialmente cuando se quiere escribir código más claro o usar chequeo estático de tipos 
(por ejemplo, con herramientas como mypy o editores tipo VSCode).

1. Any
Representa cualquier tipo de dato. Literalmente, puede ser un int, str, list, dict, una clase, lo que sea.
   Ejemplo:
        def imprimir(valor: Any) -> None:
            print(valor)
        
        - Acá [valor] puede ser cualquier cosa, y el tipado lo permite.

2.Optional[T]
Significa que el valor puede ser del tipo T o None.
    Ejemplo:
        def obtener_nombre() -> Optional[str]:
            if hay_nombre:
               return "Pepe"
            else:
               return None
        
        - Esto indica que esta función puede devolver un str o None.

¿Por qué se usa en tu clase?
- push(self, value: Any) acepta cualquier tipo de dato.
- pop(self) -> Optional[Any] indica que puede devolver un dato (de cualquier tipo) o None si la pila está vacía.

Lo mismo para on_top.
'''

class Stack:
    def __init__(self): #Este es el constructor de la clase. Se ejecuta automáticamente cuando creás una nueva instancia.
        self.__elements = []

        '''  
        Inicializa una lista vacía __elements que va a almacenar los elementos de la pila.
        El doble guion bajo (__) indica que es un atributo privado. 
        '''

    def push(self, value: Any) -> None: #Este método agrega un valor a la pila, usándolo como push (lo pone al final de la lista).
        self.__elements.append(value)

    def pop(self) -> Optional[Any]:
        return (
            self.__elements.pop()
            if self.__elements
            else None
        )
        '''
        Este método saca y devuelve el último elemento agregado a la pila (el del tope).
        Si la pila está vacía, devuelve None.
        '''

    def size(self) -> int: #Devuelve la cantidad de elementos en la pila.
        return len(self.__elements)

    def on_top(self) -> Optional[Any]: 
        return (
            self.__elements[-1]
            if self.__elements
            else None
        )
        '''
        Devuelve el elemento que está en la cima de la pila, sin eliminarlo.
        Si la pila está vacía, devuelve None.
        '''

    def show(self): #Este método muestra los elementos de la pila sin alterarla. Lo hace así:
        aux_stack = Stack() #Crea una pila auxiliar para guardar temporalmente los elementos.
        #Va sacando los elementos de la pila original, los imprime y los guarda en la auxiliar.
        while self.size() > 0: #Finalmente, vuelve a poner los elementos en la pila original.
            value = self.pop()
            print(value)
            aux_stack.push(value)
        
        while aux_stack.size() > 0:
            self.push(aux_stack.pop())

    def peek(self):  # <--- Nueva funcion
        if self.size() > 0 :
            return self.items[-1]
        else:
            raise IndexError("Peek from empty stack")

'''
- Este codigo implementa una clase Stack que permite:
  1. Agregar elementos - (push).
  2. Sacar elementos - (pop).
  3. Ver cuántos hay - (size).
  4. Ver el que está en la cima - (on_top).
  5. Mostrar todos los elementos sin perderlos - (show).
  6. peek - (ver el último elemento sin sacarlo).
'''