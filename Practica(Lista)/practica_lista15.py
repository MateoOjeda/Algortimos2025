# 15. 

from ClaseLista import List

lista_entrenadore = List()

entrenadores = [
    ["Ash", 5, 10, 90, [
        ["Pikachu", 50, "eléctrico", ""],
        ["Charizard", 70, "fuego", "volador"],
        ["Bulbasaur", 40, "planta", "veneno"],
        ["Squirtle", 35, "agua", ""],
        ["Snorlax", 60, "normal", ""],
        ["Charizard", 70, "fuego", "volador"]
    ]],
    ["Misty", 2, 15, 35, [
        ["Psyduck", 25, "agua", ""],
        ["Starmie", 45, "agua", "psíquico"]
    ]],
    ["Brock", 4, 8, 60, [
        ["Onix", 55, "roca", "tierra"],
        ["Geodude", 30, "roca", "tierra"],
        ["Tyrantrum", 80, "roca", "dragón"]
    ]],
    ["Cynthia", 6, 3, 120, [
        ["Garchomp", 88, "dragón", "tierra"],
        ["Lucario", 75, "lucha", "acero"],
        ["Roserade", 68, "planta", "veneno"],
        ["Gastrodon", 66, "agua", "tierra"],
        ["Togekiss", 65, "hada", "volador"],
        ["Milotic", 72, "agua", ""]
    ]],
    ["Red", 3, 5, 55, [
        ["Charizard", 70, "fuego", "volador"],
        ["Blastoise", 68, "agua", ""],
        ["Venusaur", 67, "planta", "veneno"],
        ["Terrakion", 75, "roca", "lucha"],
        ["Snorlax", 60, "normal", ""],
        ["Pidgeot", 60, "normal", "volador"]
    ]],
    ["Erika", 4, 6, 40, [
        ["Vileplume", 42, "planta", "veneno"],
        ["Bellossom", 40, "planta", ""]
    ]],
    ["Wallace", 2, 4, 18, [
        ["Milotic", 75, "agua", ""],
        ["Luvdisc", 30, "agua", ""]
    ]],
    ["Lance", 7, 2, 150, [
        ["Dragonite", 85, "dragón", "volador"],
        ["Gyarados", 80, "agua", "volador"],
        ["Aerodactyl", 78, "roca", "volador"],
        ["Charizard", 80, "fuego", "volador"],
        ["Salamence", 84, "dragón", "volador"],
        ["Altaria", 76, "dragón", "volador"]
    ]],
    ["Steven", 6, 3, 110, [
        ["Metagross", 88, "acero", "psíquico"],
        ["Aggron", 80, "acero", "roca"],
        ["Claydol", 75, "tierra", "psíquico"],
        ["Skarmory", 78, "acero", "volador"],
        ["Armaldo", 72, "roca", "bicho"],
        ["Cradily", 70, "roca", "planta"]
    ]],
    ["Gary", 3, 6, 60, [
        ["Umbreon", 58, "siniestro", ""],
        ["Nidoking", 65, "veneno", "tierra"],
        ["Scizor", 68, "bicho", "acero"],
        ["Arcanine", 66, "fuego", ""]
    ]],
    ["May", 2, 7, 30, [
        ["Torchic", 28, "fuego", ""],
        ["Beautifly", 32, "bicho", "volador"]
    ]],
    ["Roxanne", 1, 8, 20, [
        ["Nosepass", 40, "roca", ""],
        ["Geodude", 35, "roca", "tierra"]
    ]],
    ["Nate", 5, 5, 100, [
        ["Samurott", 72, "agua", ""],
        ["Archeops", 70, "roca", "volador"],
        ["Zoroark", 75, "siniestro", ""],
        ["Wingull", 22, "agua", "volador"]
    ]],
    ["Iris", 4, 4, 75, [
        ["Haxorus", 78, "dragón", ""],
        ["Excadrill", 74, "tierra", "acero"],
        ["Emolga", 65, "eléctrico", "volador"]
    ]],
    ["Bruno", 6, 2, 130, [
        ["Hitmonlee", 70, "lucha", ""],
        ["Hitmonchan", 68, "lucha", ""],
        ["Machamp", 75, "lucha", ""],
        ["Onix", 70, "roca", "tierra"]
    ]]
]

for entren in lista_entrenadore:
    lista_entrenadore.insert(entren)

print("- Lista de entrenadores Pokemon -")
lista_entrenadore.show()

# A
def cantidad_pokemon(entrenadores, nombre_entrenador):
    for entrenador in entrenadores:
        if entrenador[0] == nombre_entrenador:
            return len(entrenador[4])
    return 0
int_nombre = input("ingrese nombre del entrenador: ")
print(f"cantidad de pokemon es {cantidad_pokemon(entrenadores,int_nombre)}")

# B
def entrenadores_torneos(entrenadores):
    resultados = []
    for entrenador in entrenadores:
        if entrenador[1] > 3:
            resultados.append(entrenadores[0])

    return resultados

print("entrenadores con mas de 3 torneos ganados: ", entrenadores_torneos(entrenadores))

# C
def pokemon_mayor_nivel(entrenadores):
    if not entrenadores:
        return None
    # c.1 encontrar al entrenador con mayor cantidad de torneos ganados
    max_torneos= -1
    entrenador_max = None
    for entrenador in entrenadores:
        if entrenador[1] > max_torneos:
            max_torneos = entrenador[1]
            entrenador_max = entrenador
        
    # c.2 en su lista encotrar el pokemon de mayor nivel
    pokemon = entrenador_max[4]
    if not pokemon:
        return None
    max_nivel = -1
    pokemon_max = None
    for pokemo in pokemon:
        if pokemo[1] > max_nivel:
            max_nivel = pokemo[1]
            pokemon_max = pokemo
    return pokemon_max

print("pokemon de mayor nivel del entrenador con mayor cantidad de torneos ganados: ", pokemon_mayor_nivel(entrenadores))

# D
def datos_entrenador(entrenadores, nombre_entrenador):
    for entrenador in entrenadores:
        if entrenador[0] == nombre_entrenador:
            print(f"Entrenador: {entrenador[0]}")
            print(f"Torneos Ganados: {entrenador[1]}")
            print(f"Batallas Perdidas: {entrenador[2]}")
            print(f"Batallas Ganadas: {entrenador[3]}")
            print("Pokemon: ")
            for pokemon in entrenador[4]:
                subtipo = f", subtipo:{ pokemon[3]}" if pokemon[3] else ""
                print(f" -{pokemon[0]} (Nivel : {pokemon[1]}, Tipo: {pokemon[2]}{subtipo}))")
            return
    print("Emtremador no encontrado")  

datos_entrenador(entrenadores , input("ingrese nombre del entrenador: "))  

# E
def entrenadores_porc(entrenadores, umbral=79):
    resultados = []
    for entrenador in entrenadores:
        ganadas = entrenador[1]
        perdidas = entrenador[2]
        total = ganadas + perdidas
        if total > 0:
            porcentaje = (ganadas / total) *100
            if porcentaje > umbral:
                resultados.append(entrenador[0])
    return resultados

entrenadores_porc(entrenadores)

# F
def entrenadores_tipo(entrenadores):
    resultado = []
    for entrenador in entrenadores:
        tiene_tipo = False
        for pokemon in entrenador[4]:
            tipo = pokemon[2]
            subtipo = pokemon[3]
            if(tipo =="fuego" and subtipo == "planta") or (tipo == "Agua" and subtipo == "Volador"):
                tiene_tipo = True
                break
            if tiene_tipo:
                resultado.append(entrenador[0])
    return resultado

entrenadores_tipo(entrenadores)

# G
def promedio_nivel_pokemons(entrenadores, nombre_entrenador):
    for entrenador in entrenadores:
        if entrenador[0] == nombre_entrenador:
            pokemons = entrenador[4]
            if not pokemons:
                return 0.0
            suma_niveles = sum(pokemon[1] for pokemon in pokemons)
            return suma_niveles / len(pokemons)
    return 0.0

promedio_nivel_pokemons(entrenadores, "Ash")

# H
def entrenadores_con_pokemon(entrenadores, nombre_pokemon):
    conteo = 0
    for entrenador in entrenadores:
        for pokemon in entrenador[4]:
            if pokemon[0] == nombre_pokemon:
                conteo += 1
                break  # Solo una vez por entrenador
    return conteo

entrenadores_con_pokemon(entrenadores, "Pikachu")

# I
def entrenadores_repetidos(entrenadores):
    resultado = []
    for entrenador in entrenadores:
        nombres_pokemons = [pokemon[0] for pokemon in entrenador[4]]
        if len(nombres_pokemons) != len(set(nombres_pokemons)):
            resultado.append(entrenador[0])
    print("Entrenadores con Pokémons repetidos:", resultado)

entrenadores_repetidos(entrenadores)


# J
def entrenadores_pokemons_especificos(entrenadores):
    pokemons_buscados = ["Tyrantrum", "Terrakion", "Wingull"]
    resultado = []
    for entrenador in entrenadores:
        for pokemon in entrenador[4]:
            if pokemon[0] in pokemons_buscados:
                resultado.append(entrenador[0])
                break
    return list(set(resultado))  # Elimina duplicados

entrenadores_pokemons_especificos(entrenadores)

# K
def verificar_pokemon_entrenador(entrenadores, nombre_entrenador, nombre_pokemon):
    for entrenador in entrenadores:
        if entrenador[0] == nombre_entrenador:
            for pokemon in entrenador[4]:
                if pokemon[0] == nombre_pokemon:
                    print(f"Si {nombre_entrenador} tiene a {nombre_pokemon}.")
                    print(f"Datos entrenador: Nombre: {entrenador[0]}, Torneos: {entrenador[1]}, Perdidas: {entrenador[2]}, Ganadas: {entrenador[3]}")
                    subtipo_str = f", Subtipo: {pokemon[3]}" if pokemon[3] else ""
                    print(f"Datos Pokémon: {pokemon[0]} (Nivel: {pokemon[1]}, Tipo: {pokemon[2]}{subtipo_str})")
                    return
            print(f"{nombre_entrenador} no tiene a {nombre_pokemon}.")
            return
    print(f"Entrenador '{nombre_entrenador}' no encontrado.")

verificar_pokemon_entrenador(entrenadores, nombre_entrenador=input("ingrese nombre del entrenador: "), nombre_pokemon=input("ingrese nombre del pokemon: "))