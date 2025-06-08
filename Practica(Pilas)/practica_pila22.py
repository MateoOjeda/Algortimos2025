# 22. Se recuperaron las bitácoras de las naves del cazarrecompensas Boba Fett y Din Djarin (The
#     Mandalorian), las cuales se almacenaban en una pila (en su correspondiente nave) en cada 
#     misión de caza que emprendió, con la siguiente información: planeta visitado, a quien capturó, 
#     costo de la recompensa. Resolver las siguientes actividades: 
#     a. mostrar los planetas visitados en el orden que hicieron las misiones cada uno de los cazzarrecompensas;
#     b. determinar cuántos créditos galácticos recaudo en total cada cazarrecompensas y de estos quien obtuvo mayor fortuna;
#     c. determinar el número de la misión –es decir su posición desde el fondo de la pila– en la que Boba Fett capturo a Han Solo, suponga que dicha misión está cargada;
#     d. indicar la cantidad de capturas realizadas por cada cazarrecompensas.

from ClasesPilas import Stack

lista_boba = [
    {"planeta": "Tatooine", "captura": "Han Solo", "costo": 50000},
    {"planeta": "Jakku", "captura": "Rey", "costo": 100000},
    {"planeta": "Hoth", "captura": "Luke Skywalker", "costo": 200000},
    {"planeta": "Endor", "captura": "Leia Organa", "costo": 150000},
    {"planeta": "Bespin", "captura": "Lando Calrissian", "costo": 80000},
    {"planeta": "Dagobah", "captura": "Yoda", "costo": 300000}
]
lista_din =[
    {"planeta": "Tatooine", "captura": "Grogu", "costo": 100000},
    {"planeta": "Mandalore", "captura": "Bo-Katan Kryze", "costo": 200000},
    {"planeta": "Coruscant", "captura": "Ahsoka Tano", "costo": 150000},
    {"planeta": "Naboo", "captura": "Padmé Amidala", "costo": 250000},
    {"planeta": "Mustafar", "captura": "Anakin Skywalker", "costo": 300000},
    {"planeta": "Kamino", "captura": "Jango Fett", "costo": 50000}
]

pila_boba = Stack()
pila_din = Stack()

for mision in lista_boba:
    pila_boba.push(mision)

for mision in lista_din:
    pila_din.push(mision)

print("- Misiones de boba fett: ")
pila_boba.show() # mostramos los elementos de la pila
print("-----------------------------------------")
print("- Misiones de din djarin: ")
pila_din.show() # mostramos los elementos de la pila

# a. mostrar los planetas visitados en el orden que hicieron las misiones cada uno de los cazzarrecompensas;
pila_boba_planetas = Stack()
pila_boba_aux = Stack()

while pila_boba.size() > 0:
    mision = pila_boba.pop()
    pila_boba_planetas.push(mision["planeta"])
    pila_boba_aux.push(mision)

while pila_boba_aux.size() > 0:
    pila_boba.push(pila_boba_aux.pop())

print("PUNTO A")
print("1 - Planetas visitados por Boba Fett:")
pila_boba_planetas.show()
print("++++++++++++++++++++++++++++++++++++++++++++++++")

pila_din_planetas = Stack()
pila_din_aux = Stack()

while pila_din.size() > 0:
    mision = pila_din.pop()
    pila_din_planetas.push(mision["planeta"])
    pila_din_aux.push(mision)

while pila_din_aux.size() > 0:
    pila_din.push(pila_din_aux.pop())

print("2 - Planetas visitados por Din Djarin:")
pila_din_planetas.show()
print("-------------------------------------------------------------------")

# b. determinar cuántos créditos galácticos recaudo en total cada cazarrecompensas y de estos quien obtuvo mayor fortuna;
pila_boba_creditos = Stack()
pila_boba_aux_2 = Stack()
suma_creditos_boba = 0

while pila_boba.size() > 0:
    mision_din = pila_boba.pop()

    suma_creditos_boba = mision_din["costo"] + suma_creditos_boba
    pila_boba_creditos.push(suma_creditos_boba)

    pila_boba_aux_2.push(mision_din)

while pila_boba_aux_2.size() > 0:
    pila_boba.push(pila_boba_aux_2.pop())

print("PUNTO B")
print("1 - Creditos galacticos recaudados por Boba Fett: ", suma_creditos_boba)
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

pila_din_creditos = Stack()
pila_din_aux_2 = Stack()
suma_creditos_din = 0

while pila_din.size() > 0:
    mision = pila_din.pop()

    suma_creditos_din = mision["costo"] + suma_creditos_din
    pila_din_creditos.push(suma_creditos_din)

    pila_din_aux_2.push(mision)

while pila_din_aux_2.size() > 0:
    pila_din.push(pila_din_aux_2.pop())

print("2 - Creditos galacticos recaudados por Din Djarin: ", suma_creditos_din)
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

if suma_creditos_boba > suma_creditos_din:
    print("- Boba Fett obtuvo mayor fortuna")
else: 
    print("- Din Djarin obtuvo mayor fortuna")
print("-------------------------------------------------------------------")

# c. determinar el número de la misión –es decir su posición desde el fondo de la pila– en la que Boba Fett capturo a Han Solo, suponga que dicha misión está cargada;
posicion_han_solo = None
contador = 0
pila_aux_han = Stack()

tamano_pila = pila_boba.size()  # Esto es necesario para convertir la posición desde el tope a desde el fondo

while pila_boba.size() > 0:
    mision = pila_boba.pop()
    contador += 1
    pila_aux_han.push(mision)

    if mision["captura"].lower() == "han solo":
        # Posición desde el fondo = tamaño pila - (posición desde el tope - 1)
        posicion_han_solo = tamano_pila - (contador - 1)
        # No rompemos el bucle porque queremos restaurar toda la pila

# Restaurar pila original
while pila_aux_han.size() > 0:
    pila_boba.push(pila_aux_han.pop())

print("PUNTO C")
if posicion_han_solo:
    print(f"- Han Solo fue capturado en la misión número {posicion_han_solo}")
else:
    print("- Han Solo no fue capturado por Boba Fett.")

print("-------------------------------------------------------------------")
# d. indicar la cantidad de capturas realizadas por cada cazarrecompensas.
pila_boba_cap = Stack()
pila_boba_aux_4 = Stack()
cant_cap_boba = 0

while pila_boba.size() > 0:
    mision = pila_boba.pop()
    if mision["captura"] != "":
        cant_cap_boba = cant_cap_boba + 1
    pila_boba_cap.push(mision)

while pila_boba_aux_4.size() > 0:
    pila_boba.push(pila_boba_aux_4.pop())

print("PUNTO D")
print("1 - Cantidad de capturas realizadas por Boba Fett: ", cant_cap_boba)
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

pila_din_cap = Stack()
pila_din_aux_4 = Stack()
cant_cap_din = 0

while pila_din.size() > 0:
    mision = pila_din.pop()
    if mision["captura"] != "":
        cant_cap_din = cant_cap_din + 1
    pila_din_cap.push(mision)

while pila_din_aux_4.size() > 0:
    pila_din.push(pila_din_aux_4.pop())

print("2 - Cantidad de capturas realizadas por Din Djarin: ", cant_cap_din)
print("-------------------------------------------------------------------")