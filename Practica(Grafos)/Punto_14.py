from ClaseGrafo import Graph

# Implementar sobre un grafo no dirigido los algoritmos necesario para dar solución a las siguientes
# tareas:
# a. cada vértice representar un ambiente de una casa: cocina, comedor, cochera, quincho,
# baño 1, baño 2, habitación 1, habitación 2, sala de estar, terraza, patio;
# b. cargar al menos tres aristas a cada vértice, y a dos de estas cárguele cinco, el peso de la arista
# es la distancia entre los ambientes, se debe cargar en metros;
# c. obtener el árbol de expansión mínima y determine cuantos metros de cables se necesitan
# para conectar todos los ambientes;
# d. determinar cuál es el camino más corto desde la habitación 1 hasta la sala de estar para
# determinar cuántos metros de cable de red se necesitan para conectar el router con el
# Smart Tv.

from ClaseGrafo import Graph

# GRAFO NO DIRIGIDO
g = Graph(is_directed=True)

# a) Vértices (ambientes de la casa)
ambientes = [
    "cocina", "comedor", "cochera", "quincho",
    "baño 1", "baño 2", "habitación 1", "habitación 2",
    "sala de estar", "terraza", "patio"
]

for a in ambientes:
    g.insert_vertex(a)

#-------------------------------------------------------------
# b) Cargar aristas [al menos 3 por vertice, y dos vertices con 5 aristas]
# Distancias en metros

# Cocina
g.insert_edge("cocina", "comedor", 4)
g.insert_edge("cocina", "patio", 6)
g.insert_edge("cocina", "baño 1", 5)
g.insert_edge("cocina", "habitación 1", 9)     # extra para que tenga 4

# Comedor [tendria 5 conexiones]
g.insert_edge("comedor", "sala de estar", 3)
g.insert_edge("comedor", "habitación 2", 7)
g.insert_edge("comedor", "baño 2", 6)
g.insert_edge("comedor", "terraza", 10)
# Ya tenia comedor – cocina → total 5

# Cochera
g.insert_edge("cochera", "patio", 8)
g.insert_edge("cochera", "quincho", 12)
g.insert_edge("cochera", "sala de estar", 15)

# Quincho [tendria 5 conexiones]
g.insert_edge("quincho", "terraza", 9)
g.insert_edge("quincho", "patio", 7)
g.insert_edge("quincho", "baño 1", 11)
# Ya tenia quincho – cochera → total 4
# Una mas:
g.insert_edge("quincho", "habitación 2", 13)

# Baño 1
g.insert_edge("baño 1", "baño 2", 5)
g.insert_edge("baño 1", "habitación 1", 4)
# Ya tenia baño1 – cocina, baño1 – quincho → total 4

# Baño 2
g.insert_edge("baño 2", "habitación 2", 6)
# Ya tenia baño2 – comedor, baño2 – baño1 → total 3

# Habitación 1
g.insert_edge("habitación 1", "habitación 2", 5)
g.insert_edge("habitación 1", "sala de estar", 8)
# Ya tenia habitacion1 – cocina, habitacion1 – baño1 → total 4

# Habitación 2
# ya tiene varias conexiones

# Sala de estar
g.insert_edge("sala de estar", "terraza", 4)
# Ya tenia sala – comedor, sala – cochera, sala – hab1 → total 4

# Terraza
# ya tiene conexiones con comedor, quincho, sala

# Patio
# ya tiene conexiones con cocina, cochera, quincho

#-------------------------------------------------------------
# c) ARBOL DE EXPANSION MINIMA (MST) + metros de cable total

print("- Arbol de Expansion MMinima (Kruskal)")
mst = g.kruskal("cocina")
print(mst)

# extra: sumar los metros del MST
# Como tu kruskal devuelve una cadena mezclada con pesos, los extraemos

import re
pesos = list(map(int, re.findall(r"-([0-9]+)", mst)))
total_metros = sum(pesos)

print(f"Total de metros de cable necesarios para conectar todos los ambientes: {total_metros} m")

#-------------------------------------------------------------
# d) Camino mas corto entre Habitacion 1 → Sala de estar


print("- Camino mas corto Habitacion 1 → Sala de estar")

stack = g.dijkstra("habitacion 1")
distpred = {}

while stack.size() > 0:
    n, d, p = stack.pop()
    distpred[n] = (d, p)

# reconstruimos camino
camino = []
actual = "sala de estar"

if actual not in distpred:
    print("No hay camino.")
else:
    while actual is not None:
        camino.append(actual)
        if actual == "habitacion 1":
            break
        actual = distpred[actual][1]

    camino.reverse()

    print("Camino:", camino)
    print("Distancia total:", distpred["sala de estar"][0], "m")
