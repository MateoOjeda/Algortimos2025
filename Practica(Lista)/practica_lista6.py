# 6.Dada una lista de superhéroes de comics, de los cuales se conoce su nombre, año aparición,
#   casa de comic a la que pertenece (Marvel o DC) y biografía, implementar la funciones necesarias
#   para poder realizar las siguientes actividades:
#      a. eliminar el nodo que contiene la información de Linterna Verde;

#      b. mostrar el año de aparición de Wolverine;

#      c. cambiar la casa de Dr. Strange a Marvel;

#      d. mostrar el nombre de aquellos superhéroes que en su biografía menciona la palabra
#         “traje” o “armadura”;

#      e. mostrar el nombre y la casa de los superhéroes cuya fecha de aparición
#         sea anterior a 1963;

#      f. mostrar la casa a la que pertenece Capitana Marvel y Mujer Maravilla;
#     
#      g. mostrar toda la información de Flash y Star-Lord;

#      h. listar los superhéroes que comienzan con la letra B, M y S;

#      i. determinar cuántos superhéroes hay de cada casa de comic.

from ClaseLista import List  # Asegurate de importar tu clase personalizada

# Lista de superhéroes
heroes = List([
    {
        "nombre": "Wolverine",
        "anio_aparicion": 1974,
        "casa": "Marvel",
        "biografia": "Tiene un traje especial con garras"
    },
    {
        "nombre": "Dr. Strange",
        "anio_aparicion": 1963,
        "casa": "DC",
        "biografia": "Hechicero supremo con poderes misticos"
    },
    {
        "nombre": "Linterna Verde",
        "anio_aparicion": 1940,
        "casa": "DC",
        "biografia": "Portador del anillo de poder con uniforme verde"
    },
    {
        "nombre": "Capitana Marvel",
        "anio_aparicion": 1968,
        "casa": "Marvel",
        "biografia": "Guerrera intergaláctica con traje especial"
    },
    {
        "nombre": "Mujer Maravilla",
        "anio_aparicion": 1941,
        "casa": "DC",
        "biografia": "Princesa amazona con armadura mágica"
    },
    {
        "nombre": "Flash",
        "anio_aparicion": 1940,
        "casa": "DC",
        "biografia": "Corre a velocidad sobrehumana"
    },
    {
        "nombre": "Star-Lord",
        "anio_aparicion": 1976,
        "casa": "Marvel",
        "biografia": "Viaja por la galaxia con un casco tecnologico"
    },
    {
        "nombre": "Batman",
        "anio_aparicion": 1939,
        "casa": "DC",
        "biografia": "Detective con traje oscuro y capa"
    },
    {
        "nombre": "Spider-Man",
        "anio_aparicion": 1962,
        "casa": "Marvel",
        "biografia": "Joven heroe con traje rojo y azul que lanza telaranias"
    },
    {
        "nombre": "Superman",
        "anio_aparicion": 1938,
        "casa": "DC",
        "biografia": "El hombre de acero con traje azul y capa roja"
    }
])

print("- Lista de SuperHeroes -")
heroes.show()
print("-----------------------------------------------------")
#a. eliminar el nodo que contiene la información de Linterna Verde;
print("- Punto a - Eliminar Linterna Verde -")

heroes.add_criterion("nombre", lambda x: x["nombre"])

eliminado = heroes.delete_value("Linterna Verde", "nombre")
if eliminado:
    print(f"eliminado correctamente: {eliminado}")
else:
    print("Linterna verde no fue encontrado en la lista")

print("-----------------------------------------------------")

#b. mostrar el año de aparición de Wolverine;
print("- Punto b - anio de aparcion de wolverine -")

anio_worlverine = heroes.search("Wolverine", "nombre")
if anio_worlverine:
    print(f"Anioo de aparicion de wolverine: {heroes[anio_worlverine]["anio_aparicion"]}")
else:
    print("Wolverine no fue encontrado en la lista")
print("-----------------------------------------------------")

#c. cambiar la casa de Dr. Strange a Marvel;
print("- Punto c - Cambiar casa de Dr. Strange a Marvel -")

dr_strange_cambio = heroes.search("Dr. Strange", "nombre")

if dr_strange_cambio:
    heroes[dr_strange_cambio]["casa"] = "Marvel"
    print(f"Casa de Dr. Strange cambia de casa a {heroes[dr_strange_cambio]["casa"]}")
else:
    print("Dr. Strange no fue encontrado en la lista")
print("-----------------------------------------------------")

#d. mostrar el nombre de aquellos superhéroes que en su biografía menciona la palabra “traje” o “armadura”;
print("- Punto d - Superheroes con trajes o armaduras -") #corregir


# print("SuperHeroes con trajes o Armaduras:")
for hero in heroes:
    bio = hero["biografia"].lower() # Convertir a minúsculas para búsqueda insensible a mayúsculas
    if "traje" in bio or "armadura" in bio:
        print(f"- Nombre: {hero["nombre"]}, Casa: {hero["casa"]}")

print("-----------------------------------------------------")

#e. mostrar el nombre y la casa de los superhéroes cuya fecha de aparición sea anterior a 1963;
print("- Punto e - superHeroes anteriores a 1963 -")

for hero in heroes:
    if hero["anio_aparicion"] < 1963:
        print(f"- Nombre: {hero["nombre"]}, Casa: {hero["casa"]}")

print("-----------------------------------------------------")

#f. mostrar la casa a la que pertenece Capitana Marvel y Mujer Maravilla;
print("- Punto f - Casa de Capitana Marvel y Mujer Maravilla -")
cap_marvel = heroes.search("Capitana Marvel", "nombre")
muj_maravilla = heroes.search("Mujer Maravilla", "nombre")

if cap_marvel:
    print(f"Capitana Marvel pertenece a la casa: {heroes[cap_marvel]["casa"]}")
else:
    print("Capitana Marvel no fue encontrado en la lista")

if muj_maravilla:
    print(f"Mujer Maravilla pertenece a la casa: {heroes[muj_maravilla]["casa"]}")  
else:
    print("Mujer Maravilla no fue encontrado en la lista")
print("-----------------------------------------------------") 

#g. mostrar toda la información de Flash y Star-Lord;
print("- Punto g - Informacion de Flash y Strar-Lord -")
flash_inf = heroes.search("Flash", "nombre")
star_lord_info = heroes.search("Star-Lord", "nombre")

if flash_inf:
    print(f"- Informacion de Flash: {heroes[flash_inf]}")
else:
    print("Flash no fue encontrado en la lista")

if star_lord_info:
    print(f"Informacion de Star-Lord: {heroes[star_lord_info]}")  
else:
    print("Star-Lord no fue encontrado en la lista")
print("-----------------------------------------------------") 

#h. listar los superhéroes que comienzan con la letra B, M y S;
letras = ('B', 'M', 'S')
superheroes_filtrados = [h["nombre"] for h in heroes if h["nombre"].strip().upper().startswith(letras)]

# Mostrar resultados
print("Superheroes que comienzan con B, M o S:")
for nombre in superheroes_filtrados:
    print("-", nombre)
print("-----------------------------------------------------")
#i. determinar cuántos superhéroes hay de cada casa de comic.

print("- Punto i - Cantidad de SuperHeroes de cada casa -")
contador_marvel = 0
contador_dc = 0

for hero in heroes:
    if hero["casa"] == "Marvel":
        contador_marvel += 1
    elif hero["casa"] == "DC":
        contador_dc += 1

print(f"- Cantidad de SuperHeroes de Marvel: {contador_marvel}")
print(f"- Cantidad de SuperHeroes de DC: {contador_dc}")

print("-----------------------------------------------------")