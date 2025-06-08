# 20. Realizar un algoritmo que registre los movimientos de un robot, los datos que se guardan son
# cantidad de pasos y dirección 
# – suponga que el robot solo puede moverse en ocho direcciones: norte, sur, este, oeste, noreste, noroeste, sureste y suroeste–. 
# - Luego desarrolle otro algoritmo que genere la secuencia de movimientos necesarios para hacer volver al robot a su lugar de
#   partida, retornando por el mismo camino que fue.

from ClasesPilas import Stack

lista_movimientos =[
    {"pasos": 5,"direccion": "norte"},
    {"pasos": 3,"direccion": "noreste"},
    {"pasos": 2,"direccion": "sur"},
    {"pasos": 4,"direccion": "suroeste"},
    {"pasos": 1,"direccion": "este"},
    {"pasos": 6,"direccion": "noroeste"},
    {"pasos": 2,"direccion": "oeste"}
]

pila_mov = Stack()

for mov in lista_movimientos:
    pila_mov.push(mov)

print("- Movimientos del robot - ") 
pila_mov.show() # mostramos los elementos de la pila
print("-----------------------------------------")

# Diccionario de direcciones opuestas
direccion_opuesta = {
    "norte": "sur",
    "sur": "norte",
    "este": "oeste",
    "oeste": "este",
    "noreste": "suroeste",
    "noroeste": "sureste",
    "sureste": "noroeste",
    "suroeste": "noreste"
}

print("- Movimiento de regreso al punto de partida -")
while pila_mov.size() > 0:
    mov = pila_mov.pop()
    direccion_inv = direccion_opuesta[mov["direccion"]]
    print(f"{mov['pasos']} pasos hacia {direccion_inv}")