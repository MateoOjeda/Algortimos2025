# 12. Desarrollar un algoritmo que elimine el anteúltimo nodo de una lista independientemente de
#     la información del mismo, utilizando lista simplemente enlazada y después con lista doblemente
#     enlazada

class NodoSimple:

    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None 

class ListaSimple:
    
    def __init__(self):
        self.cabeza = None

    def agregar(self, dato):
        nuevo = NodoSimple(dato)
        if not self.cabeza:
            self.cabeza = nuevo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo

    def eliminar_anteultimo(self):
        #Si la lista tiene menos de dos elementos no se puede eliminar el anteultimo
        if not self.cabeza or not self.cabeza.siguiente:
            print("- Lista muy corta no hay anteultimo nodo para eliminar")
            return
        
        #caso en especial: si hay solo dos nodos elimina el primero (anteultimo)
        if not self.cabeza.siguiente.siguiente:
            self.cabeza = self.cabeza.siguiente
            return
        
        #recorre para encontrar nodo anterior al anteultimo
        actual = self.cabeza
        while actual.siguiente and actual.siguiente.siguiente and actual.siguiente.siguiente.siguiente:
            actual = actual.siguiente

        # "actual" es el nodo anterior al anteultimo
        # actual.siguiente es el anteultimo
        # actual.siguiente.siguiente es el ultimo

        # Saltamos el anteultimo
        actual.siguiente = actual.siguiente.siguiente

    def mostrar(self):
        actual = self.cabeza
        while actual:
            print(actual.dato, end=" -> ")
            actual = actual.siguiente
        print("None")

#ejemplo de uso
print("---- Lista Simple ----")
lista = ListaSimple()
for i in [1,2,3,4,5]:
    lista.agregar(i)

print("- Lista Original -")
lista.mostrar()

print("- Lista despues de eliminar el anteultimo nodo:")
lista.mostrar()

class NodoDoble: 
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
        self.anterior = None

class ListaDoble:
    def __init__(self):
        self.cabeza = None

    def agregar(self, dato):
        nuevo = NodoDoble(dato)
        if not self.cabeza:
            self.cabeza = nuevo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo
            nuevo.anterior = actual

    def eliminar_anteultimo(self):
        #Si la lista tiene menos de dos elementos no se puede eliminar el anteultimo
        if not self.cabeza or not self.cabeza.siguiente:
            print("- Lista muy corta no hay anteultimo nodo para eliminar")
            return
        
        #caso en especial: si hay solo dos nodos elimina el primero (anteultimo)
        if not self.cabeza.siguiente.siguiente:
            self.cabeza = self.cabeza.siguiente
            return
        
        #recorre para encontrar nodo anterior al anteultimo
        actual = self.cabeza
        while actual.siguiente and actual.siguiente.siguiente and actual.siguiente.siguiente.siguiente:
            actual = actual.siguiente

        # "actual" es el nodo anterior al anteultimo
        # actual.siguiente es el anteultimo
        # actual.siguiente.siguiente es el ultimo

        # Saltamos el anteultimo
        actual.siguiente = actual.siguiente.siguiente

    def mostrar(self):
        actual = self.cabeza
        while actual:
            print(actual.dato, end=" <-> ")
            actual = actual.siguiente
        print("None")

# ejemplo de uso
print("---- Lista Doble enlasada ----")

lista_doble = ListaDoble()
for i in [1,2,3,4,5]:
    lista_doble.agregar(i)

print("- Lista doble Original")
lista_doble.mostrar()

lista_doble.eliminar_anteultimo()

print("- Lista doble despues de eliminar el anteultimo nodo")
lista_doble.mostrar()
