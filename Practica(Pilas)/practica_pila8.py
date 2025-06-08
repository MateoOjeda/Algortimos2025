# 8. Dada una pila de cartas de las cuales se conoce su número y palo,–que representa un mazo de
#    cartas de baraja española–,resolver las siguientes actividades:
#    a. generar las cartas del mazo de forma aleatoria;
#    b. separar la pila mazo en cuatro pilas una por cada palo;
#    c. ordenar una de las cuatro pilas (espada, basto, copa u oro) de manera creciente.

# mazo de cartas: 40 cartas (10 de cada palo) - [basto, oro, copas, espadas] - [1, 2, 3, 4, 5, 6, 7, 10, 11, 12]

from random import randint
from random import shuffle
from ClasesPilas import Stack

# generamos la funcion de mazo
def generar_mazo():
    palos = ["Basto","Espada","Oro","Copa"]
    valores = [1, 2, 3, 4, 5, 6, 7, 10, 11, 12]
    mazo_cartas = [(valor, palo) for palo in palos for valor in valores]
    shuffle(mazo_cartas) # mezclamos el mazo de cartas
    return mazo_cartas

def palos_distintos(pila_mazo):
    basto_pila = Stack() 
    oro_pila = Stack()
    copa_pila = Stack()
    espada_pila = Stack()

    while pila_mazo.size() > 0:
        cartas = pila_mazo.pop()
        if cartas[1] == "Basto":
            basto_pila.push(cartas)
        elif cartas[1] == "Espada":
            espada_pila.push(cartas)
        elif cartas[1] == "Oro":
            oro_pila.push(cartas)
        elif cartas[1] == "Copa":
            copa_pila.push(cartas)

    return basto_pila, espada_pila, oro_pila, copa_pila

def ordenar_pilas(pila):
    cartas = []
    while pila.size() > 0:
        cartas.append(pila.pop())

    cartas.sort(key=lambda x: x[0]) # ordenamos por el valor de la carta

    for carta in cartas:
        pila.push(carta)

# programa principal
mazo_de_cartas = generar_mazo() 
pila_mazo = Stack()

for cartas in mazo_de_cartas:
    pila_mazo.push(cartas)

print("- Mazo de cartas - ")
pila_mazo.show() # mostramos los elementos de la pila   

# Separo la pila de cartas por palos
basto_pila, espada_pila, oro_pila, copa_pila = palos_distintos(pila_mazo)

print("- Cartas separadda por palos -")
print("- Basto: ")
basto_pila.show()
print("- Oro: ")
oro_pila.show()
print("- Copa:")
copa_pila.show()
print("- Espada: ")
espada_pila.show()

ordenar_pilas(basto_pila)
ordenar_pilas(oro_pila)
ordenar_pilas(copa_pila)
ordenar_pilas(espada_pila)

print("- Cartas separadda por palos (Ordenadas) -")
print("- Basto (Ordenadas): ")
basto_pila.show()
print("- Oro (Ordenadas): ")
oro_pila.show()
print("- Copa (Ordenadas):")
copa_pila.show()
print("- Espada (Ordenadas): ")
espada_pila.show()