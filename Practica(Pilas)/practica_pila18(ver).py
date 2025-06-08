# 18. Dada una pila de objetos de una oficina de los que se dispone de su nombre y peso (por ejemplo
#     monitor 1 kg, teclado 0.25 kg, silla 7 kg, etc.), ordenar dicha pila de acuerdo a su peso –del
#     objeto más liviano al más pesado–. Solo pueden utilizar pilas auxiliares como estructuras extras,
#     no se pueden utilizar métodos de ordenamiento.

from ClasesPilas import Stack

def ordenar_peso(pila):
    """
    Ordena una pila de objetos de acuerdo a su peso, del más liviano al más pesado.
    
    :param pila: Pila de objetos con nombre y peso.
    :return: Pila ordenada por peso.
    """
    pila_aux = Stack()
    
    while pila.size() > 0:
        # Sacar un objeto de la pila original
        peso = pila.pop()
        
        # Mover los objetos de la pila auxiliar a la pila original si son más pesados
        while (pila_aux.size() > 0) and (peso[1] < pila_aux.peek()[1]): # el peek sirve para ver el peso sin sacar el objeto
            pila.push(pila_aux.pop())
        
        # Colocar el objeto en la pila auxiliar
        pila_aux.push(peso)
    
    # Devolver la pila auxiliar a la original
    while pila_aux.size() > 0:
        pila.push(pila_aux.pop())
    
    return pila

pila_pesos = Stack()

for i in range(4):
    print(f"Objeto {i+1}:")
    nombre_obj = input("- Ingrese el nombre del objeto: " )
    peso_obj = float(input("- Ingrese el peso del Objeto: "))

    pila_pesos.push((nombre_obj, peso_obj))

print("- Pila Original: ")
pila_pesos.show()

ordenar_peso(pila_pesos)
print("- Pila Ordenada: ")  
pila_pesos.show()
