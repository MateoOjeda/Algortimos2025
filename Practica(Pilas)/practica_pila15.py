# 16. Se tienen dos pilas con personajes de Star Wars, en una los del episodio V de “The empire
#     strikes back” y la otra los del episodio VII “The force awakens”. Desarrollar un algoritmo que 
#     permita obtener la intersección de ambas pilas, es decir los personajes que aparecen en ambos
#     episodios.

from ClasesPilas import Stack

pila_episodio_v = Stack()
pila_episodio_vii = Stack()

ep_v_nombres = ['Luke Skywalker', 'Leia Organa', 'Han Solo', 'Boba Fett', 'Darth Vader']
ep_vii_nombres = ['Rey', 'Finn', 'Poe Dameron', 'Leia Organa', 'Kylo Ren']

for nombre in ep_v_nombres:
    pila_episodio_v.push(nombre)

for nombre in ep_vii_nombres:
    pila_episodio_vii.push(nombre)

print("- Personajes del episodio V: ")
pila_episodio_v.show()

print("- Personajes del episodio VII: ")
pila_episodio_vii.show()

# Buscar intersección
interseccion = []
aux_v = Stack()
aux_vii = Stack()

# Convertir pila VII a lista temporal (para comparar fácilmente)
lista_vii = []

while pila_episodio_vii.size() > 0:
    personaje = pila_episodio_vii.pop()
    lista_vii.append(personaje)
    aux_vii.push(personaje)

# Restaurar pila VII
while aux_vii.size() > 0:
    pila_episodio_vii.push(aux_vii.pop())

# Recorrer pila V y comparar con lista_vii
while pila_episodio_v.size() > 0:
    personaje_v = pila_episodio_v.pop()
    if personaje_v in lista_vii and personaje_v not in interseccion:
        interseccion.append(personaje_v)
    aux_v.push(personaje_v)

# Restaurar pila V
while aux_v.size() > 0:
    pila_episodio_v.push(aux_v.pop())

# Mostrar resultados
print("- Personajes en ambos episodios:")
for personaje in interseccion:
    print(personaje)

