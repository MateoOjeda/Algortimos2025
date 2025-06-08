# # 7. Implementar los algoritmos necesarios para resolver las siguientes tareas:
#      
#      a. concatenar dos listas, una atrás de la otra;
#      
#      b. concatenar dos listas en una sola omitiendo los datos repetidos y manteniendo su orden;
#      
#      c. contar cuántos elementos repetidos hay entre dos listas, es decir la intersección de ambas;
#      
#      d. eliminar todos los nodos de una lista de a uno a la vez mostrando su contenido.

from ClaseLista import List

lista_animales_dom = List()
lista_animales_gran = List()

animales_domesticos = ["perro","gato","loro","conejo","hamster","pez dorado","tortuga","canario"]
animales_varios = ["vaca","cerdo","oveja","caballo","gallina","loro","perro","gato"]

for animal in animales_domesticos:
    lista_animales_dom.append(animal)


for animal in animales_varios:
    lista_animales_gran.append(animal)

print("- Lista de animales domesticos -")
lista_animales_dom.show()
print("--------------------------------")
print("- Lista de animales de granja -")
lista_animales_gran.show()
print("--------------------------------")

#a. concatenar dos listas, una atrás de la otra;  
print("- Punto A") 
lista_animales_total = List()
lista_animales_total.extend(lista_animales_dom) #extend agrega los elementos de la lista al final de la lista actual
lista_animales_total.extend(lista_animales_gran)
print("- Lista de animales total -")
lista_animales_total.show()
print("--------------------------------")

#b. concatenar dos listas en una sola omitiendo los datos repetidos y manteniendo su orden;    
print("- Punto B")
lista_animales_unicos = List()

for animal in lista_animales_dom + lista_animales_gran:
    if animal not in lista_animales_unicos:
        lista_animales_unicos.append(animal)

print("- Lista de animales domesticos sin repetir -")
lista_animales_unicos.show()
print("--------------------------------")  

#c. contar cuántos elementos repetidos hay entre dos listas, es decir la intersección de ambas;  
print("- Punto C -")
interseccion_cartas = List()
contador_inter = 0

for animal in lista_animales_dom + lista_animales_gran:
    if animal in lista_animales_dom and animal in lista_animales_gran:
        contador_inter += 1

print(f"Cantidad de animales repetidos entre las dos listas: {contador_inter}")
print("--------------------------------")

#d. eliminar todos los nodos de una lista de a uno a la vez mostrando su contenido.
print("- Punto D -")
print("- Eliminando nodo uno a uno -")

while len(lista_animales_dom) > 0:
    eliminado = lista_animales_dom.pop(0) # Elimina el primer elemento de la lista
    print(f"Eliminando: {eliminado}")

print("- Lista vacia -")
