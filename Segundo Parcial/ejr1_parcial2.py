# Ejercicio 1: Se tiene los datos de Pokémons de las 9 generaciones cargados de manera aleatoria (1025 en total) 
# de los cuales se conoce su nombre, número, tipo/tipos, debilidad frente a tipo/tipos, si tiene mega evolucion (bool) 
# y si tiene forma gigamax (bool) para el cual debemos construir tres árboles para acceder de manera eficiente a los 
# datos contemplando lo siguiente:
# * los índices de cada uno de los árboles deben ser nombre, número y tipo;
# * mostrar todos los datos de un Pokémon a partir de su número y nombre –para este último, 
#   la búsqueda debe ser por proximidad, es decir si busco “bul” se deben mostrar todos los Pokémons 
#   cuyos nombres comiencen o contengan dichos caracteres–;
# * mostrar todos los nombres de los Pokémons de un determinado tipo: fantasma, fuego, acero y eléctrico;
# * realizar un listado en orden ascendente por número y nombre de Pokémon, y además un listado por nivel por nombre;
# * mostrar todos los Pokémons que son débiles frente a Jolteon, Lycanroc y Tyrantrum;
# * mostrar todos los tipos de Pokémons y cuántos hay de cada tipo;
# * determinar cuantos Pokémons tienen megaevolucion.
# * determinar cuantos Pokémons tiene forma gigamax.

from ClaseArbol import BinaryTree

pokemons = [
    {
        "nombre": "Charmander",
        "numero": 4,
        "tipos": ["fuego"],
        "debilidad": ["agua", "tierra", "roca"],
        "mega": False,
        "gigamax": False
    },
    {
        "nombre": "Charizard",
        "numero": 6,
        "tipos": ["fuego", "volador"],
        "debilidad": ["roca", "agua", "electrico"],
        "mega": True,
        "gigamax": True
    },
    {
        "nombre": "Arcanine",
        "numero": 59,
        "tipos": ["fuego"],
        "debilidad": ["agua", "tierra", "roca"],
        "mega": False,
        "gigamax": False
    },
    {
        "nombre": "Gastly",
        "numero": 92,
        "tipos": ["fantasma", "veneno"],
        "debilidad": ["fantasma", "siniestro", "psiquico"],
        "mega": False,
        "gigamax": False
    },
    {
        "nombre": "Gengar",
        "numero": 94,
        "tipos": ["fantasma", "veneno"],
        "debilidad": ["fantasma", "siniestro", "tierra"],
        "mega": True,
        "gigamax": True
    },
    {
        "nombre": "Mimikyu",
        "numero": 778,
        "tipos": ["fantasma", "hada"],
        "debilidad": ["acero", "fantasma"],
        "mega": False,
        "gigamax": False
    },
    {
        "nombre": "Steelix",
        "numero": 208,
        "tipos": ["acero", "tierra"],
        "debilidad": ["fuego", "agua", "lucha"],
        "mega": True,
        "gigamax": False
    },
    {
        "nombre": "Aggron",
        "numero": 306,
        "tipos": ["acero", "roca"],
        "debilidad": ["agua", "lucha", "tierra"],
        "mega": True,
        "gigamax": False
    },
    {
        "nombre": "Lucario",
        "numero": 448,
        "tipos": ["lucha", "acero"],
        "debilidad": ["fuego", "tierra", "lucha"],
        "mega": True,
        "gigamax": False
    },
    {
        "nombre": "Pikachu",
        "numero": 25,
        "tipos": ["electrico"],
        "debilidad": ["tierra"],
        "mega": False,
        "gigamax": True
    },
    {
        "nombre": "Jolteon",
        "numero": 135,
        "tipos": ["electrico"],
        "debilidad": ["tierra"],
        "mega": False,
        "gigamax": False
    },
    {
        "nombre": "Raichu",
        "numero": 26,
        "tipos": ["electrico"],
        "debilidad": ["tierra"],
        "mega": False,
        "gigamax": False
    },
    {
        "nombre": "Lycanroc",
        "numero": 745,
        "tipos": ["roca"],
        "debilidad": ["lucha", "tierra", "agua", "acero"],
        "mega": False,
        "gigamax": False
    },
    {
        "nombre": "Tyrantrum",
        "numero": 697,
        "tipos": ["roca", "dragon"],
        "debilidad": ["hielo", "lucha", "tierra", "hada", "dragon"],
        "mega": False,
        "gigamax": False
    },
    {
        "nombre": "Bulbasaur",
        "numero": 1,
        "tipos": ["planta", "veneno"],
        "debilidad": ["fuego", "psiquico", "hielo"],
        "mega": False,
        "gigamax": False
    },
    {
        "nombre": "Squirtle",
        "numero": 7,
        "tipos": ["agua"],
        "debilidad": ["electrico", "planta"],
        "mega": False,
        "gigamax": False
    },
    {
        "nombre": "Blastoise",
        "numero": 9,
        "tipos": ["agua"],
        "debilidad": ["electrico", "planta"],
        "mega": True,
        "gigamax": True
    },
    {
        "nombre": "Eevee",
        "numero": 133,
        "tipos": ["normal"],
        "debilidad": ["lucha"],
        "mega": False,
        "gigamax": True
    },
    {
        "nombre": "Sylveon",
        "numero": 700,
        "tipos": ["hada"],
        "debilidad": ["acero", "veneno"],
        "mega": False,
        "gigamax": False
    },
    {
        "nombre": "Dragonite",
        "numero": 149,
        "tipos": ["dragon", "volador"],
        "debilidad": ["hielo", "hada", "roca", "dragon"],
        "mega": False,
        "gigamax": False
    },
    {
        "nombre": "Houndoom",
        "numero": 229,
        "tipos": ["fuego", "siniestro"],
        "debilidad": ["agua", "tierra", "roca"],
        "mega": True,
        "gigamax": False
    },
    {
        "nombre": "Metagross",
        "numero": 376,
        "tipos": ["acero", "psiquico"],
        "debilidad": ["fuego", "tierra", "fantasma", "siniestro"],
        "mega": True,
        "gigamax": False
    },
    {
        "nombre": "Garchomp",
        "numero": 445,
        "tipos": ["dragon", "tierra"],
        "debilidad": ["hielo", "hada"],
        "mega": True,
        "gigamax": False
    },
    {
        "nombre": "Snorlax",
        "numero": 143,
        "tipos": ["normal"],
        "debilidad": ["lucha"],
        "mega": False,
        "gigamax": True
    },
]


arbol_nombre = BinaryTree()
arbol_numero = BinaryTree()
arbol_tipo = BinaryTree()

for p in pokemons:
    # arbol por nombre
    arbol_nombre.insert(p["nombre"], p)

    # arbol por numero
    arbol_numero.insert(p["numero"], p)

    # arbol por tipo → un Pokemon puede tener mas de un tipo
    for t in p["tipos"]:
        # Clave compuesta: tipo + nombre
        arbol_tipo.insert(t + "-" + p["nombre"], p)


# 1) MOSTRAR DATOS DE UN POKEMON POR NUMERO
def mostrar_por_numero(num):
    nodo = arbol_numero.search(num)
    if nodo:
        print("Pokemon encontrado:")
        print(nodo.other_values)
    else:
        print("No existe ese numero.")

# 2) BÚSQUEDA POR NOMBRE (PROXIMIDAD)
def buscar_por_nombre(prefijo):
    print(f"Pokemon que contienen '{prefijo}':")
    arbol_nombre.proximity_search(prefijo)

# 3) MOSTRAR TODOS LOS POKEMON DE CIERTOS TIPOS
def mostrar_por_tipo(tipo):
    print(f"\nPokemon de tipo {tipo}:")
    arbol_tipo.proximity_search(tipo + "-")

# 4) LISTADOS EN ORDEN ASCENDENTE Y POR NIVELES
def listado_por_numero():
    print("\nListado ASCENDENTE por numero:")
    arbol_numero.in_order()

def listado_por_nombre():
    print("\nListado ASCENDENTE por nombre:")
    arbol_nombre.in_order()

def listado_por_niveles_nombre():
    print("\nListado POR NIVELES:")
    arbol_nombre.by_level()

# 5) POKEMON DEBILES A JOLTEON, LYCANROC, TYRANTRUM
def debiles_a(lista_nombres):
    print("\nPokemon debiles a:", lista_nombres)
    for pk in pokemons:
        for objetivo in lista_nombres:
            nodo = arbol_nombre.search(objetivo)
            if nodo:
                tipos_ataque = nodo.other_values["tipos"]
                if any(t in pk["debilidad"] for t in tipos_ataque):
                    print(pk["nombre"])
    print()

# 6) CONTAR POKEMON POR TIPO
def contar_por_tipo():
    print("\nCantidad de Pokemon por tipo:")
    conteo = {}
    for p in pokemons:
        for t in p["tipos"]:
            conteo[t] = conteo.get(t, 0) + 1
    for tipo, cantidad in conteo.items():
        print(tipo, ":", cantidad)

# 7) CONTAR MEGAEVOLUCIONES
def contar_megas():
    print("\nCantidad de Pokemon con Mega Evolucion:")
    print(sum(1 for p in pokemons if p["mega"]))

# 8) CONTAR GIGAMAX
def contar_gigamax():
    print("\nCantidad de Pokemon Gigamax:")
    print(sum(1 for p in pokemons if p["gigamax"]))

print("---- PRUEBAS ----")

nombre_po = input("- ingrese el pokemon que quiere buscar: ")
buscar_por_nombre(nombre_po)
mostrar_por_tipo("fuego")
listado_por_numero()
debiles_a(["Jolteon"])
contar_por_tipo()
contar_megas()
contar_gigamax()