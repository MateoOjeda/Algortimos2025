# 19. Dada una pila de películas de las que se conoce su título, estudio cinematográfico y año de estreno, 
# desarrollar las funciones necesarias para resolver las siguientes actividades:
#    a. mostrar los nombre películas estrenadas en el año 2014;
#    b. indicar cuántas películas se estrenaron en el año 2018;
#    c. mostrar las películas de Marvel Studios estrenadas en el año 2016.

from ClasesPilas import Stack

pila_peliculas = Stack()

peliculas = [
    {"titulo": "Interstellar", "estudio": "Paramount Pictures", "anio": 2014},
    {"titulo": "Guardians of the Galaxy", "estudio": "Marvel Studios", "anio": 2014},
    {"titulo": "Zootopia", "estudio": "Walt Disney Pictures", "anio": 2016},
    {"titulo": "Doctor Strange", "estudio": "Marvel Studios", "anio": 2016},
    {"titulo": "Black Panther", "estudio": "Marvel Studios", "anio": 2018},
    {"titulo": "Aquaman", "estudio": "Warner Bros.", "anio": 2018},
    {"titulo": "Avengers: Infinity War", "estudio": "Marvel Studios", "anio": 2018},
    {"titulo": "The Shape of Water", "estudio": "Fox Searchlight Pictures", "anio": 2017},
    {"titulo": "Dunkirk", "estudio": "Warner Bros.", "anio": 2017},
    {"titulo": "The Revenant", "estudio": "20th Century Fox", "anio": 2015}
]


for pelicula in peliculas:
    pila_peliculas.push(pelicula)

#  a. mostrar los nombre películas estrenadas en el año 2014;
pila_aux = Stack()
pila_peliculas_2014 = Stack()

while pila_peliculas.size() > 0:
    pelicula = pila_peliculas.pop() 
    if pelicula["anio"] == 2014:
        pila_peliculas_2014.push(pelicula["titulo"])
    pila_aux.push(pelicula)

while pila_aux.size() > 0: #reconstruimos la pila original
    pila_peliculas.push(pila_aux.pop())

print("A. Peliculas estrenadas en 2014:")
pila_peliculas_2014.show()

# b. indicar cuántas películas se estrenaron en el año 2018;
pila_aux_2 = Stack()
contador_peliculas = 0

while pila_peliculas.size() > 0:
    pelicula = pila_peliculas.pop() 
    if pelicula["anio"] == 2018:
        contador_peliculas += 1
    pila_aux_2.push(pelicula)

while pila_aux.size() > 0: #reconstruimos la pila original
    pila_peliculas.push(pila_aux.pop())

print("-----------------------------------------")
print("B. Cantidad de peliculas estrenadas en 2018:")
print("- ",contador_peliculas)

# c. Marvel Studios en 2016
pila_aux_c = Stack()
pila_peliculas_marvel = Stack()

while pila_peliculas.size() > 0:
    pelicula = pila_peliculas.pop() 
    if pelicula["anio"] == 2016 and pelicula["estudio"].strip() == "Marvel Studios":
        pila_peliculas_marvel.push(pelicula["titulo"])
    pila_aux_c.push(pelicula)

while pila_aux_c.size() > 0:
    pila_peliculas.push(pila_aux_c.pop())

print("-----------------------------------------")
print("C. Peliculas de Marvel Studios estrenadas en 2016:")
pila_peliculas_marvel.show()