#Ejercicio 1: 
# Dado una lista simple de python (array) de 15 superheroes realizar dos funciones recursivas:
#   a. funcion recursiva  para buscar, determinar si Capitan America esta en la lista.
#   b. funcion recursiva para listar los superheroes de la lista.

from ClaseLista import List

superheroes = [
    "Iron Man", "Thor", "Hulk", "Viuda Negra", "Ojo de Halcon",
    "Capitan America", "Spiderman", "Ant-Man", "Pantera Negra",
    "Doctor Strange", "Bruja Escarlata", "Vision", "Falcon",
    "Soldado del Invierno", "Capitana Marvel"
]

# a. funcion recursiva  para buscar, determinar si Capitan America esta en la lista.
def buscar_personaje(lista, indice = 0):
    if indice >= len(lista):
        return False
    if lista[indice] == "Capitan America":
        return True
    return buscar_personaje(lista, indice + 1)

# b. funcion recursiva para listar los superheroes de la lista.

def lista_superheroes(lista, indice = 0):
    if indice >= len(lista):
        return
    print(lista[indice])
    lista_superheroes(lista, indice + 1)

# ejecucion del programa
print("- Lista de SuperHeroes -")
lista_superheroes(superheroes)
print("- -------------------- -")
print("- Esta el personaje Capitan America?:", buscar_personaje(superheroes))