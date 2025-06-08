# 10. Insertar el nombre de la diosa griega Atenea en la i-ésima posición debajo de la cima de una 
# pila con nombres de dioses griegos.

from ClasesPilas import Stack

def insertar_dios(pila, elemento, ipos):
    pila_aux = Stack()
    contador = 0
     
    # muevo los elementos de la pila original a la pila auxiliar
    while pila.size() > 0:
        pila_aux.push(pila.pop())
        contador += 1
    
    # pongo el nuevo elemeto en la pila original
    pila.push(elemento)

    # restauro los elementos a la pila original
    while pila_aux.size() > 0:
        pila.push(pila_aux.pop())

dioses_griegos = Stack()
# Pila de dioses griegos
dioses_griegos.push("Apolo")
dioses_griegos.push("Zeus")
dioses_griegos.push("Hades") 
dioses_griegos.push("Poseidon") 
dioses_griegos.push("Hera")
dioses_griegos.push("Demeter")
dioses_griegos.push("Ares")
dioses_griegos.push("Hermes")
dioses_griegos.push("Atenea") # Atenea es la diosa griega de la sabiduría y la guerra

print("- Pila de dioses Griegos: ") 
dioses_griegos.show()

# incerto atenea en la posicion dos por debajo de la cima 
insertar_dios(dioses_griegos, "Atenea", 2)

print("- Pila de dioses Griegos despuus de insertar Atenea: ")
dioses_griegos.show()