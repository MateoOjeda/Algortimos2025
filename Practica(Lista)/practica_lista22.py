from ClaseLista import List

lista_jedi = List()

jedi = [
    ["Ahsoka Tano", ["Anakin Skywalker"], ["blanco"], "Togruta"],
    ["Kit Fisto", ["Klaatu"], ["verde"], "Nautolan"],
    ["Yoda", [], ["verde"], "Desconocida"],
    ["Luke Skywalker", ["Obi-Wan Kenobi", "Yoda"], ["verde", "azul"], "Humano"],
    ["Qui-Gon Jinn", ["Count Dooku"], ["verde"], "Humano"],
    ["Mace Windu", ["Tholme"], ["violeta"], "Humano"],
    ["Obi-Wan Kenobi", ["Qui-Gon Jinn"], ["azul"], "Humano"],
    ["Plo Koon", ["Klaatu"], ["azul"], "Kel Dor"],
    ["Shaak Ti", ["Klaatu"], ["rojo"], "Togruta"],
    ["Aayla Secura", ["Kit Fisto"], ["azul"], "Twi'lek"],
    ["Barriss Offee", ["Luminara Unduli"], ["verde"], "Mirialan"],
    ["Anakin Skywalker", ["Obi-Wan Kenobi"], ["azul", "rojo"], "Humano"],
]

for j in jedi:
    lista_jedi.append(j)

# a. listado ordenado por nombre y por especie;
def lista_ordenada(lista, criterio):
    if criterio == "nombre":
        lista_ordenada = sorted(lista, key=lambda j: j[0])
    elif criterio == "especie":
        lista_ordenada = sorted(lista, key=lambda j: j[3])
    else:
        print("Criterio no válido")
        return

    print(f"\nLista ordenada por {criterio}:")
    for j in lista_ordenada:
        print(j)

    return lista_ordenada

# b. mostrar toda la información de Ahsoka Tano y Kit Fisto;
def mostrar_info(lista, nombres):
    print("\nInformación solicitada de Jedi:")
    for nombre in nombres:
        encontrado = next((j for j in lista if j[0] == nombre), None)
        if encontrado:
            print(encontrado)
        else:
            print(f"{nombre} no encontrado en la lista")

# c. mostrar todos los padawan de Yoda y Luke Skywalker, es decir sus aprendices;
def mostrar_padawans(lista, maestros):
    padawans = [j for j in lista if any(m in j[1] for m in maestros)]
    print(f"\nPadawans de {', '.join(maestros)}:")
    for p in padawans:
        print(p)
    return padawans

# d. mostrar los Jedi de especie humana y twi'lek;
def mostrar_especie(lista, especies):
    especies_lower = [e.lower() for e in especies]
    filtrados = [j for j in lista if j[3].lower() in especies_lower]
    print(f"\nJedi de especie {', '.join(especies)}:")
    for j in filtrados:
        print(j)
    return filtrados

# e. listar todos los Jedi que comienzan con A;
def lista_ordenada_inicial(lista, inicial):
    filtrados = [j for j in lista if j[0].startswith(inicial)]
    print(f"\nJedi que comienzan con '{inicial}':")
    for j in filtrados:
        print(j)
    return filtrados

# f. mostrar los Jedi que usaron sable de luz de más de un color;
def sables_color(lista):
    filtrados = [j for j in lista if len(j[2]) > 1]
    print("\nJedi que usaron sables de luz de más de un color:")
    for j in filtrados:
        print(j)
    return filtrados

# g. indicar los Jedi que utilizaron sable de luz amarillo o violeta;
def sable_colores(lista, colores):
    colores_lower = [c.lower() for c in colores]
    filtrados = [j for j in lista if any(c.lower() in colores_lower for c in j[2])]
    print(f"\nJedi que usaron sable de luz de color {', '.join(colores)}:")
    for j in filtrados:
        print(j)
    return filtrados

# h. indicar los nombre de los padawans de Qui-Gon Jinn y Mace Windu, si los tuvieron.
def nombres_padawans(lista, maestros):
    padawans = [j[0] for j in lista if any(m in j[1] for m in maestros)]
    print(f"\nNombres de padawans de {', '.join(maestros)}:")
    if padawans:
        for p in padawans:
            print(p)
    else:
        print("No tienen padawans registrados.")
    return padawans

# Pruebas
lista_ordenada(lista_jedi, "nombre")
lista_ordenada(lista_jedi, "especie")
mostrar_info(lista_jedi, ["Ahsoka Tano", "Kit Fisto"])
mostrar_padawans(lista_jedi, ["Yoda", "Luke Skywalker"])
mostrar_especie(lista_jedi, ["Humano", "Twi'lek"])
lista_ordenada_inicial(lista_jedi, "A")
sables_color(lista_jedi)
sable_colores(lista_jedi, ["amarillo", "violeta"])
nombres_padawans(lista_jedi, ["Qui-Gon Jinn", "Mace Windu"])
