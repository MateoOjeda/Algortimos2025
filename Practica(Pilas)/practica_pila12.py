# 12. Dada una pila con nombres de los personajes de la saga de Star Wars, implemente una función
# que permita determinar si Leia Organa o Boba Fett están en dicha pila sin perder los datos.

from ClasesPilas import Stack

def buscar_personaje(pila: Stack, personaje: str) -> bool:
    pila_aux = Stack()
    encontrado = False

    while pila.size() > 0:
        nombre = pila.pop()
        if nombre == personaje:
            encontrado = True
        pila_aux.push(nombre)

    while pila_aux.size() > 0:
        pila.push(pila_aux.pop())

    return encontrado

# Crear la pila y agregar personajes
personajes_pila = Stack()

nombres = ['Luke Skywalker', 'Leia Organa', 'Han Solo', 'Boba Fett', 'Darth Vader']

for nombre in nombres:
    personajes_pila.push(nombre)

print("- Pila de personajes: ")
personajes_pila.show()

# Buscar personajes
nombre_1 = 'Leia Organa'
nombre_2 = 'Boba Fett'

if buscar_personaje(personajes_pila, nombre_1) or buscar_personaje(personajes_pila, nombre_2):
    print("- Personaje encontrado en la pila.")


