# Se cuenta con una lista de películas de cada una de estas se dispone de los siguientes datos:
# nombre, valoración del público –es un valor comprendido entre 0-10–, año de estreno y recaudación.
# Desarrolle los algoritmos necesarios para realizar las siguientes tareas:
# a. permitir filtrar las películas por año –es decir mostrar todas las películas de un determinado
# año–;
# b. mostrar los datos de la película que más recaudo;
# c. indicar las películas con mayor valoración del público, puede ser más de una;
# d. mostrar el contenido de la lista en los siguientes criterios de orden –solo podrá utilizar una
# lista auxiliar–:
# I. por nombre,
# II. por recaudación,
# III. por año de estreno,
# IV. por valoración del público.

from ClaseLista import list

lista_pelicualas = list()
# Crear la lista de películas
peliculas = [
    {"nombre": "Pelicula A", "valoracion": 8.5, "anio": 2020, "recaudacion": 1500000},
    {"nombre": "Pelicula B", "valoracion": 9.0, "anio": 2019, "recaudacion": 2000000},
    {"nombre": "Pelicula C", "valoracion": 7.5, "anio": 2020, "recaudacion": 1800000},
    {"nombre": "Pelicula D", "valoracion": 9.0, "anio": 2018, "recaudacion": 2200000},
    {"nombre": "Pelicula E", "valoracion": 6.0, "anio": 2019, "recaudacion": 1000000},
]

for pelicula in peliculas:
    lista_pelicualas.insertar(peliculas, "nombre")

# a.
def peliculas_anios(lista, anio):
    return [p for p in lista if p["anio"] == anio]

# b.
def pelicula_mas_recaudado(lista):
    return max(lista, key=lambda p: p["recaudacion"])

# c.
def pelicula_mejor_valoracion(lista):
    if not lista:
        return []
    max_valoracion = max(p["valoracion"] for p in lista)
    return [p for p in lista if p["valoracion"] == max_valoracion]
    return max(lista, key=lambda p: p["recaudacion"])

# d.
def mostrar_ordenado(lista, criterio):
    lista_aux = list(lista) # creo una lista auxiliar
    lista_aux.add_criterion("nombre", lambda p: p["nombre"])
    lista_aux.add_criterion("valoracione", lambda p: p["valoracion"])
    lista_aux.add_criterion("anio", lambda p :p["anio"])
    lista_aux.add_criterion("recaudacion", lambda p: p["recaudacion"])

    lista_aux.sort_by_criterion(criterio)
    print(f"\nPelículas ordenadas por {criterio}:")
    for p in lista_aux:
        print(p)