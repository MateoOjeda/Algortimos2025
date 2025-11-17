from typing import Any, Optional

class Queue:

    def __init__(self):
        self.__elements = []

    def arrive(self, value: Any) -> None: # Agregar un elemento al final de la cola.
        self.__elements.append(value)

    def attention(self) -> Optional[Any]: #Atender (remover y retornar) al primer elemento de la cola.
        return (
            self.__elements.pop(0)
            if self.__elements
            else None
        )

    def size(self) -> int: # Retorna la cantidad de elementos en la cola.
        return len(self.__elements)
    
    def on_front(self) -> Optional[Any]: # Retorna el primer elemento de la cola sin removerlo.
        return (
            self.__elements[0]
            if self.__elements
            else None
        )

    def move_to_end(self) -> Optional[Any]: # Mueve el primer elemento de la cola al final.
        if self.__elements:
            value = self.attention()
            self.arrive(value)
            return value
    
    def show(self): # Muestra los elementos de la cola.
        for i in range(len(self.__elements)):
            print(self.move_to_end())

    def copy(self):
        q = Queue()
        for item in self.items:
            q.arrive(item)
        return q