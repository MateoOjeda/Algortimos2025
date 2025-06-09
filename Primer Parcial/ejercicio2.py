# Ejercicio 2: 
# Dada una lista de personajes de marvel (la desarrollada en clases) debe tener 100 o mas, resolver:
# a. Listado ordenado de manera ascendente por nombre de los personajes.
# b. Determinar en que posicion esta The Thing y Rocket Raccoon.
# c. Listar todos los villanos de la lista.
# d. Poner todos los villanos en una cola para determinar luego cuales aparecieron antes de 1980.
# e. Listar los superheores que comienzan con  Bl, G, My, y W.
# f. Listado de personajes ordenado por nombre real de manera ascendente de los personajes.
# g. Listado de superheroes ordenados por fecha de aparación.
# h. Modificar el nombre real de Ant Man a Scott Lang.
# i. Mostrar los personajes que en su biografia incluyan la palabra time-traveling o suit.
# j. Eliminar a Electro y Baron Zemo de la lista y mostrar su información si estaba en la lista

from ClaseLista import List
from ClaseCola import Queue
from super_heroes_data import superheroes 

personajes = List(superheroes)

# añado los criterios de orden y busqueda

personajes.add_criterion("name", lambda x: x["name"])
personajes.add_criterion("real_name", lambda x: x["real_name"] or "")
personajes.add_criterion("first_appearance", lambda x: x["first_appearance"])

# a. Listado ordenado de manera ascendente por nombre de los personajes.
personajes.sort_by_criterion("name")
listado_odernado_nom = [p["name"] for p in personajes]

# b. Determinar en que posicion esta The Thing y Rocket Raccoon.
pos_personaje_the_thing = personajes.search("The Thing", "name")
pos_personaje_rocket = personajes.search("Rocket Raccoon", "name")

# c. Listar todos los villanos de la lista.
personajes_villanos = [p for p in personajes if p["is_villain"]]

# d. Poner todos los villanos en una cola para determinar luego cuales aparecieron antes de 1980.
cola_villanos = Queue()
for v in personajes_villanos:
    cola_villanos.arrive(v)

villanos_1980 = []
for __ in range(cola_villanos.size()):
    villano = cola_villanos.move_to_end()
    if villano["first_appearance"] < 1980:
        villanos_1980.append(villano["name"])

# e. Listar los superheores que comienzan con  Bl, G, My, y W.
prefijos = ("Bl", "G", "My", "W")
filtro_superheroes = [
    p["name"] for p in personajes if p["name"].startswith(prefijos) 
]

# f. Listado de personajes ordenado por nombre real de manera ascendente de los personajes.
personajes.sort_by_criterion("real_name")
lista_nombres_reales = [(p["name"], p["real_name"]) for p in personajes]

# g. Listado de superheroes ordenados por fecha de aparación.
personajes.sort_by_criterion("first_appearance")
lista_aparcion_superheroe = [(p["name"], p["first_appearance"]) for p in personajes]

# h. Modificar el nombre real de Ant Man a Scott Lang.
modificar_personaje = personajes.search("Ant Man", "name")
if modificar_personaje is not None:
    personajes[modificar_personaje]["real_name"] = "Scott Lang"
    antman_modificado = personajes[modificar_personaje]
else:
    antman_modificado = None

# i. Mostrar los personajes que en su biografia incluyan la palabra time-traveling o suit.
personajes_biografia = ["time-traveling", "suit"]
coincidencia_biografia = [
    p for p in personajes if any (k in p["short_bio"] for k in personajes_biografia)
]

# j. Eliminar a Electro y Baron Zemo de la lista y mostrar su información si estaba en la lista
info_personaje_electro = personajes.delete_value("Electro", "name")
info_personaje_zemo = personajes.delete_value("Baron Zemo", "name")

# Resultado Final:
print("- Punto A. Lista ordenada por nombre: ")
print( listado_odernado_nom)
print("--------------------------------------------------------------")
print("- Punto B. Posicion de los personajes the thing y rocket: ")
print("- The Thing: ", pos_personaje_the_thing)
print("- Rocket Raccon: ",pos_personaje_rocket)
print("--------------------------------------------------------------")
print("- Punto C. Lista de todos los villanos: ")
print(personajes_villanos)
print("--------------------------------------------------------------")
print("- Punto D. Villanos que aparecieron despues de 1980: ")
print(villanos_1980)
print("--------------------------------------------------------------")
print("- Punto E. Listado de los superheores que comienzan con  Bl, G, My, y W: ")
print(filtro_superheroes)
print("--------------------------------------------------------------")
print("- Punto F. Listado de personajes por nombre real:")
print(lista_nombres_reales)
print("--------------------------------------------------------------")
print("- Punto G. Listado de superheroes ordenados por aparcion:")
print(lista_aparcion_superheroe)
print("--------------------------------------------------------------")
print("- Punto H. Modificar el nombre de un personaje: ")
print(antman_modificado)
print("--------------------------------------------------------------")
print("- Punto I. Personajes que en la biografia aparece time-traveling o suit:")
print(coincidencia_biografia)
print("--------------------------------------------------------------")
print("- Punto J. Eliminar personajes: ")
print("- Electro: ",info_personaje_electro)
print("- Baron Zemo: ", info_personaje_zemo)
print("--------------------------------------------------------------")