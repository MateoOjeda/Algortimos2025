#1. Diseñar un algoritmo que permita contar la cantidad de nodos de una lista.

from ClaseLista import List

lista_ariculos = List()

articulos_limpieza = [
    "Detergente",
    "Lavandina",
    "Desinfectante",
    "Jabón en polvo",
    "Esponja",
    "Trapo de piso",
    "Escoba",
    "Recogedor",
    "Baldes",
    "Guantes de látex",
    "Limpiavidrios",
    "Lustra muebles",
    "Toallas de papel",
    "Paño de microfibra",
    "Cepillo de cerdas",
    "Ambientador",
    "Desengrasante",
    "Limpiador multiuso",
    "Limpiador de inodoros",
    "Bolsas de basura"
]



for articulo in articulos_limpieza:
    lista_ariculos.append(articulo)

print("Lista de artículos de limpieza:")
for articulo in lista_ariculos:
    print(articulo)

print("-------------------------------")
print("Cantidad de nodos en la lista: ", len(lista_ariculos))

