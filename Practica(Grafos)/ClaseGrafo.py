from typing import Any, Optional

from Claseheap import HeapMin
from ClaseLista import List
from ClaseCola import Queue
from ClaseStack import Stack


class Graph(List):
    # Clase Graph que hereda de List (suponemos que List es una lista enlazada/estructura
    # ya implementada en list_.py). Esta clase modela un grafo con vértices y aristas

    class __nodeVertex:
        # Clase interna que representa un vértice del grafo

        def __init__(self, value: Any, other_values: Optional[Any] = None):
            # value: identificador del vértice (ej: 'A', 'B', 1, etc.)
            # other_values: campo opcional para guardar información adicional
            self.value = value
            # edges: lista de aristas salientes desde este vértice
            self.edges = List()
            # Se agregan criterios de orden para la lista de aristas: por 'value' y por 'weight'
            # (se asume que List tiene un método add_criterion que permite ordenar/filtrar)
            self.edges.add_criterion('value', Graph._order_by_value)
            self.edges.add_criterion('weight', Graph._order_by_weight)
            self.other_values = other_values
            # visited: flag útil para recorridos (DFS/BFS)
            self.visited = False
        
        def __str__(self):
            # Representación en string del vértice (se imprime su value)
            return self.value
    
    class __nodeEdge:
        # Clase interna que representa una arista (edge) hacia un destino con un peso

        def __init__(self, value: Any, weight: Any, other_values: Optional[Any] = None):
            # value: identificador del vértice destino
            # weight: costo/peso de la arista
            self.value = value
            self.weight = weight
            self.other_values = other_values # no esta en uso aun
        
        def __str__(self):
            # String representativo de la arista
            return f'Destination: {self.value} with weight --> {self.weight}'
    
    def __init__(self, is_directed=False):
        # Inicializador del grafo
        # is_directed: booleano que indica si el grafo es dirigido
        # Agregamos criterio de orden para los vértices por su 'value'
        self.add_criterion('value', self._order_by_value)
        self.is_directed = is_directed

    def _order_by_value(item):
        # Función usada como criterio de orden para listas: ordena por .value
        return item.value

    def _order_by_weight(item):
        # Función usada como criterio de orden para listas de aristas: ordena por .weight
        return item.weight
    
    def show(
        self
    ) -> None:
        # Muestra por pantalla todos los vértices y sus aristas
        for vertex in self:
            print(f"Vertex: {vertex}")
            vertex.edges.show() 

    def insert_vertex(
        self,
        value: Any,
    ) -> None:
        # Inserta un nuevo vértice en el grafo
        # Crea un objeto __nodeVertex y lo agrega a la lista (self es una List de vértices)
        node_vertex = Graph.__nodeVertex(value)
        self.append(node_vertex)

    def insert_edge(self, origin_vertex: Any, destination_vertex: Any, weight: int) -> None:
        # Inserta una arista desde origin_vertex hacia destination_vertex con un peso
        # Busca las posiciones (índices) de los vértices origen y destino
        
        origin = self.search(origin_vertex, 'value')
        destination = self.search(destination_vertex, 'value')
        if origin is not None and destination is not None:
            # Crea un nodo de arista apuntando al valor del destino
            node_edge = Graph.__nodeEdge(destination_vertex, weight)
            # Agrega la arista a la lista de aristas del vértice origen
            self[origin].edges.append(node_edge)
            # ATENCIÓN: la lógica aquí revisa self.is_directed y luego agrega otra arista
            # Esto es inusual: si el grafo es dirigido (is_directed True) normalmente NO se
            # agregaría la arista inversa. Si se quiere un grafo NO dirigido debería comprobarse
            # "if not self.is_directed". Mantengo el código original, pero es probable que
            # esto sea un error lógico según la intención del autor.
            if self.is_directed and origin != destination:
                # Si entra aquí, añade la arista inversa en el vértice destino
                node_edge = Graph.__nodeEdge(origin_vertex, weight)
                self[destination].edges.append(node_edge)
        else:
            # Al menos uno de los vértices no existe en el grafo
            print('no se puede insertar falta uno de los vertices')

    def delete_edge(
        self,
        origin,
        destination,
        key_value: str = None,
    ) -> Optional[Any]:
        # Elimina la arista (origin -> destination). key_value indica la clave para buscar
        pos_origin = self.search(origin, key_value)
        if pos_origin is not None:
            # Se delega la eliminación a la lista de aristas del vértice origen
            edge = self[pos_origin].edges.delete_value(destination, key_value)
            # Si el grafo es dirigido, también intenta eliminar la arista inversa
            # NOTA: la condición usa self.is_directed, al igual que en insert_edge, lo cual
            # puede no coincidir con la semántica esperada (ver comentario en insert_edge)
            if self.is_directed and edge is not None:
                pos_destination = self.search(destination, key_value)
                if pos_destination is not None:
                    self[pos_destination].edges.delete_value(origin, key_value)
            return edge

    def delete_vertex(
        self,
        value,
        key_value_vertex: str = None,
        key_value_edges: str = 'value',
    ) -> Optional[Any]:
        # Elimina un vértice del grafo y todas las aristas entrantes hacia ese vértice
        # IMPORTANTE: aquí hay una referencia a 'g.delete_value' en lugar de 'self.delete_value'.
        # g parece ser una variable global definida fuera de la clase; probablemente esto sea
        # un error: debería usarse self.delete_value para eliminar el vértice de este grafo.
        delete_value = g.delete_value(value, key_value_vertex)
        if delete_value is not None:
            # Si se eliminó el vértice, recorrer todos los vértices restantes y eliminar
            # aristas que apunten al vértice borrado
            for vertex in self:
                self.delete_edge(vertex.value, value, key_value_edges)
        return delete_value

    def mark_as_unvisited(self) -> None:
        # Marca todos los vértices como no visitados (útil antes de un BFS/DFS)
        for vertex in self:
            vertex.visited = False

    def exist_path(self, origin, destination):
        # Determina si existe un camino desde 'origin' hasta 'destination' usando DFS
        def __exist_path(graph, origin, destination):
            result = False
            # Buscar la posición del vértice origen
            vertex_pos = graph.search(origin, 'value')
            if vertex_pos is not None:
                if not graph[vertex_pos].visited:
                    # Marcamos como visitado y comprobamos si es el destino
                    graph[vertex_pos].visited = True
                    if graph[vertex_pos].value == destination:
                        return True
                    else:
                        # Recorremos todas las aristas salientes y aplicamos recursión
                        for edge in graph[vertex_pos].edges:
                            destination_edge_pos = graph.search(edge.value, 'value')
                            if not graph[destination_edge_pos].visited:
                                result = __exist_path(graph, graph[destination_edge_pos].value, destination)
                                if result:
                                    break
            return result
        
        self.mark_as_unvisited()
        result = __exist_path(self, origin, destination)
        return result
    
    def deep_sweep(self, value) -> None:
        # Recorrido en profundidad (DFS) que imprime los vértices visitados a partir de 'value'
        def __deep_sweep(graph, value):
            vertex_pos = graph.search(value, 'value')
            if vertex_pos is not None:
                if not graph[vertex_pos].visited:
                    graph[vertex_pos].visited = True
                    print(graph[vertex_pos])
                    for edge in graph[vertex_pos].edges:
                        destination_edge_pos = graph.search(edge.value, 'value')
                        if not graph[destination_edge_pos].visited:
                            __deep_sweep(graph, graph[destination_edge_pos].value)

        self.mark_as_unvisited()
        __deep_sweep(self, value)
        
    def amplitude_sweep(self, value)-> None:
        # Recorrido en amplitud (BFS) que imprime los vértices visitados a partir de 'value'
        queue_vertex = Queue()
        self.mark_as_unvisited()
        vertex_pos = self.search(value, 'value')
        if vertex_pos is not None:
            if not self[vertex_pos].visited:
                self[vertex_pos].visited = True
                queue_vertex.arrive(self[vertex_pos])
                while queue_vertex.size() > 0:
                    vertex = queue_vertex.attention()
                    print(vertex.value)
                    for edge in vertex.edges:
                        destination_edge_pos = self.search(edge.value, 'value')
                        if destination_edge_pos is not None:
                            if not self[destination_edge_pos].visited:
                                self[destination_edge_pos].visited = True
                                queue_vertex.arrive(self[destination_edge_pos])

    def dijkstra(self, origin):
        # Implementa Dijkstra para obtener distancias más cortas desde 'origin' a todos los
        # vértices. Retorna una pila (Stack) con información sobre las distancias y predecesores.
        
        from math import inf
        no_visited = HeapMin()
        path = Stack()
        # Inicializar heap con todos los vértices: distancia 0 para el origen, infinito para los demás
        for vertex in self:
            distance = 0 if vertex.value == origin else inf
            # Se asume que HeapMin.arrive recibe (elemento, prioridad)

            no_visited.arrive([vertex.value, vertex, None], distance)
        # Mientras haya nodos no visitados en el heap

        while no_visited.size() > 0:
            value = no_visited.attention()
            # value[0] es la distancia (prioridad), value[1] es [vertex.value, vertex, predecessor]
            
            costo_nodo_actual = value[0]
            path.push([value[1][0], costo_nodo_actual, value[1][2]])
            edges = value[1][1].edges
            for edge in edges:
                pos = no_visited.search(edge.value)
                if pos is not None:
                    if pos is not None:
                        # Si el costo por esta arista mejora la distancia en el heap, actualizar
                        if costo_nodo_actual + edge.weight < no_visited.elements[pos][0]:
                            # Actualiza el predecesor del nodo en la estructura del heap
                            no_visited.elements[pos][1][2] = value[1][0]
                            no_visited.change_priority(pos, costo_nodo_actual + edge.weight)
        return path

    def kruskal(self, origin_vertex):
        # Implementación (no totalmente estándar) del algoritmo de Kruskal para
        # construir un árbol de expansión mínima. Devuelve una representación textual
        # de los componentes/árboles.
        def search_in_forest(forest, value):
            # Busca en qué "árbol" del bosque está el vértice value
            for index, tree in enumerate(forest):
                if value in tree:
                    return index
                
        forest = []
        edges = HeapMin()
        # Inicializar: cada vértice comienza como componente en el bosque
        for vertex in self:
            forest.append(vertex.value)
            for edge in vertex.edges:
                # Se agrega cada arista al heap con su peso como prioridad
                edges.arrive([vertex.value, edge.value], edge.weight)
        
        # Mientras haya más de un componente y queden aristas
        while len(forest) > 1 and edges.size() > 0:
            edge = edges.attention()
            origin = search_in_forest(forest, edge[1][0])
            destination = search_in_forest(forest, edge[1][1])
            if origin is not None and destination is not None:
                if origin != destination:
                    # Se extraen las dos componentes y se las combina en una sola cadena
                    if origin > destination:
                        vertex_origin = forest.pop(origin)
                        vertex_destination = forest.pop(destination)
                    else:
                        vertex_destination = forest.pop(destination)
                        vertex_origin = forest.pop(origin)


                    # A partir de aquí se concatena texto para representar la nueva componente
                    # Esta representación mezcla '-' y ';' y contiene los pesos: no es una
                    # estructura estándar (por ejemplo, una lista de aristas o una lista de conjuntos),
                    # así que el resultado está pensado para imprimirse y parsearse manualmente.
                    if '-' not in vertex_origin and '-' not in vertex_destination:
                        forest.append(f'{vertex_origin}-{vertex_destination}-{edge[0]}')
                    elif '-' not in vertex_destination:
                        forest.append(vertex_origin+';'+f'{edge[1][0]}-{vertex_destination}-{edge[0]}')
                    elif '-' not in vertex_origin:
                        forest.append(vertex_destination+';'+f'{vertex_origin}-{edge[1][1]}-{edge[0]}')
                    else:
                        forest.append(vertex_origin+';'+vertex_destination+';'+f'{edge[1][0]}-{edge[1][1]}-{edge[0]}')
        
        from_vertex = search_in_forest(forest, origin_vertex)
        
        return forest[from_vertex] if from_vertex is not None else forest

def set_type(g, node_name, tipo):
    pos = g.search(node_name, 'value')
    if pos is not None:
        g[pos].other_values = tipo

def print_section(title):
    print("\n" + "="*6 + " " + title + " " + "="*6)

def dijkstra_to_dict(g, origin):
    stack = g.dijkstra(origin)
    # la clase devuelve un stack; lo vamos vaciando
    distpred = {}
    while stack.size() > 0:
        item = stack.pop()   # [vertex_name, distance, predecessor]
        distpred[item[0]] = (item[1], item[2])
    return distpred

def reconstruct_path(distpred, origin, dest):
    if dest not in distpred:
        return None
    if distpred[dest][0] == float('inf'):
        return None
    path = []
    cur = dest
    while cur is not None:
        path.append(cur)
        if cur == origin:
            break
        cur = distpred[cur][1]
    path.reverse()
    if path[0] != origin:
        return None
    return path, distpred[dest][0]
# ----------------- EJEMPLO DE USO -----------------

g = Graph(is_directed=True)

# Se insertan vértices en el grafo
g.insert_vertex('T')
g.insert_vertex('F')
g.insert_vertex('R')
g.insert_vertex('X')
g.insert_vertex('Z')
# g.insert_vertex('A')
# g.insert_vertex('B')

# Se insertan aristas con sus pesos
g.insert_edge('T', 'X', 6)
g.insert_edge('T', 'F', 3)
g.insert_edge('T', 'R', 8)
g.insert_edge('F', 'X', 2)
g.insert_edge('F', 'R', 2)
g.insert_edge('R', 'X', 5)
g.insert_edge('Z', 'R', 4)
g.insert_edge('Z', 'X', 9)
# g.insert_edge('A', 'B', 15)

# Ejemplo: comprobar si existe un camino de 'T' a 'Z'
print(g.exist_path('T', 'Z'))
