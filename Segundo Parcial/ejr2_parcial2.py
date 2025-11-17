# Ejercicio 2: Dado un grafo no dirigido con personajes de la saga Star Wars, implementar los algoritmos necesarios para resolver las siguientes tareas:
# * cada vértice debe almacenar el nombre de un personaje, las aristas representan la cantidad de episodios en los que aparecieron juntos ambos 
#   personajes que se relacionan;
# * hallar el árbol de expansión mínimo desde el vértice que contiene a: C-3PO, Yoda y Leia;
# * determinar cuál es el número máximo de episodio que comparten dos personajes, e indicar todos los pares de personajes que coinciden con 
#   dicho número;
# * cargue al menos los siguientes personajes: Luke Skywalker, Darth Vader, Yoda, Boba Fett, C-3PO, Leia, Rey, Kylo Ren, Chewbacca, Han Solo, 
#   R2-D2, BB-8;
# * calcule el camino mas ccorto desde: C-3PO a R2-D2 y desde Yoda a Darth Vader;
# * indicar qué personajes aparecieron en los nueve episodios de la saga.

from ClaseGrafo import Graph, set_type, dijkstra_to_dict, reconstruct_path
# set_type, dijkstra_to_dict, reconstruct_path es necesario si por que solo quiero usar esas funciones/clases directamente por nombre.
# Creo grafo
g_sw = Graph(is_directed=True)

# Lista minima de personajes
personajes = [
    'Luke Skywalker', 'Darth Vader', 'Yoda', 'Boba Fett', 'C-3PO', 'Leia',
    'Rey', 'Kylo Ren', 'Chewbacca', 'Han Solo', 'R2-D2', 'BB-8'
]

# Inserto los vertices
for p in personajes:
    g_sw.insert_vertex(p)

# Episodios por personaje
episodios_por_personaje = {
    'Luke Skywalker': 7,
    'Darth Vader': 4,
    'Yoda': 5,
    'Boba Fett': 2,
    'C-3PO': 9,
    'Leia': 8,
    'Rey': 3,
    'Kylo Ren': 3,
    'Chewbacca': 6,
    'Han Solo': 4,
    'R2-D2': 9,
    'BB-8': 2
}

for p, e in episodios_por_personaje.items():
    set_type(g_sw, p, e)

# Aristas con pesos = episodios compartidos 
aristas = [
    ('Luke Skywalker', 'Leia', 6),
    ('Luke Skywalker', 'Han Solo', 4),
    ('Luke Skywalker', 'Chewbacca', 5),
    ('Luke Skywalker', 'Darth Vader', 3),
    ('Leia', 'Han Solo', 4),
    ('Leia', 'C-3PO', 5),
    ('Leia', 'R2-D2', 5),
    ('Han Solo', 'Chewbacca', 6),
    ('C-3PO', 'R2-D2', 9),  
    ('C-3PO', 'Luke Skywalker', 5),
    ('R2-D2', 'Luke Skywalker', 5),
    ('Yoda', 'Luke Skywalker', 3),
    ('Yoda', 'Darth Vader', 2),
    ('Rey', 'BB-8', 2),
    ('Rey', 'Kylo Ren', 1),
    ('Kylo Ren', 'Darth Vader', 1),
    ('Boba Fett', 'Darth Vader', 1),
    ('Chewbacca', 'Leia', 3),
    ('BB-8', 'R2-D2', 1),
    ('C-3PO', 'Darth Vader', 1)
]

for o, d, w in aristas:
    g_sw.insert_edge(o, d, w)

# 1) ARBOL DE EXPACION MINIMA
print("Arbol de expansion minima (kruskal)")
for origen in ['C-3PO', 'Yoda', 'Leia']:
    mst_repr = g_sw.kruskal(origen)
    print(f"Desde '{origen}': {mst_repr}")

# 2) MAXIMO DE EPISODIOS COMPARTIDOS
max_weight = -1
pares_max = []
for vertex in g_sw:
    for edge in vertex.edges:

        if vertex.value <= edge.value:
            if edge.weight > max_weight:
                max_weight = edge.weight
                pares_max = [(vertex.value, edge.value)]
            elif edge.weight == max_weight:
                pares_max.append((vertex.value, edge.value))

print(" MAXIMO de episodios compartidos")
print(f"Maximo (ejemplo): {max_weight}")
print("Pares que alcanzan ese maximo:")
for a, b in pares_max:
    print(f" - {a}  <-->  {b}")

# 3) CAMINOS MAS CORTOS
print("Caminos mas cortos (Dijkstra)")
distpred = dijkstra_to_dict(g_sw, 'C-3PO')
res = reconstruct_path(distpred, 'C-3PO', 'R2-D2')
if res is None:
    print("No hay camino valido desde C-3PO a R2-D2")
else:
    path, cost = res
    print(f"C-3PO -> R2-D2: camino = {path}, costo (suma de pesos) = {cost}")

distpred2 = dijkstra_to_dict(g_sw, 'Yoda')
res2 = reconstruct_path(distpred2, 'Yoda', 'Darth Vader')
if res2 is None:
    print("No hay camino valido desde Yoda a Darth Vader")
else:
    path2, cost2 = res2
    print(f"Yoda -> Darth Vader: camino = {path2}, costo (suma de pesos) = {cost2}")

# 4) PERSONAJES EN 9 EPISODIOS
print("Personajes marcados con 9 episodios (ejemplo)")
appeared_9 = [v.value for v in g_sw if getattr(v, 'other_values', None) == 9]
if appeared_9:
    for p in appeared_9:
        print(f" - {p}")
else:
    print("Ningun personaje marcado con 9 episodios en estos datos de ejemplo.")
