# 5. Dado un árbol con los nombre de los superhéroes y villanos de la saga Marvel Cinematic Universe
# (MCU), desarrollar un algoritmo que contemple lo siguiente:
# a. además del nombre del superhéroe, en cada nodo del árbol se almacenará un campo booleano
# que indica si es un héroe o un villano, True y False respectivamente;
# b. listar los villanos ordenados alfabéticamente;
# c. mostrar todos los superhéroes que empiezan con C;
# d. determinar cuántos superhéroes hay el árbol;
# e. Doctor Strange en realidad está mal cargado. Utilice una búsqueda por proximidad para
# encontrarlo en el árbol y modificar su nombre;
# f. listar los superhéroes ordenados de manera descendente;
# g. generar un bosque a partir de este árbol, un árbol debe contener a los superhéroes y otro a
# los villanos, luego resolver las siguiente tareas:
# I. determinar cuántos nodos tiene cada árbol;
# II. realizar un barrido ordenado alfabéticamente de cada árbol.


# 5. Dado un árbol con los nombre de los superhéroes y villanos de la saga Marvel Cinematic Univer-
# se (MCU), desarrollar un algoritmo que contemple lo siguiente:

# a. además del nombre del superhéroe, en cada nodo del árbol se almacenará un campo boo-
# leano que indica si es un héroe o un villano, True y False respectivamente;

# b. listar los villanos ordenados alfabéticamente;
# c. mostrar todos los superhéroes que empiezan con C;
# d. determinar cuántos superhéroes hay el árbol;
# e. Doctor Strange en realidad está mal cargado. Utilice una búsqueda por proximidad para
# encontrarlo en el árbol y modificar su nombre;
# f. listar los superhéroes ordenados de manera descendente;
# g. generar un bosque a partir de este árbol, un árbol debe contener a los superhéroes y otro a
# los villanos, luego resolver las siguiente tareas:
#               I. determinar cuántos nodos tiene cada árbol;
#               II. realizar un barrido ordenado alfabéticamente de cada árbol.

superheroes = [
    {"name": "Capitana Marvel", "is_villain": False},
    {"name": "Hulk","is_villain": False},
    {"name": "Groot","is_villain": True},
    {"name": "Iron Man","is_villain": True},
    {"name": "Dr. Strange","is_villain": True},
    { "name": "Wolverine", "is_villain": False},
    {"name": "Flash","is_villain": True},
]    

from ClaseArbol import BinaryTree

arbol_super = BinaryTree()

#cargamos el arbol 
for heroes in superheroes:
    arbol_super.insert(heroes ["name"], heroes ["is_villain"]) 

print("Punto B")
arbol_super.is_villain_in_order()

print("-----------------")
print("Punto C")
arbol_super.super_in_order()
print("-----------------")

print("Punto D")
total = arbol_super.contar_heroes()
print(f"la cantidad de heroes es: {total}")

#Utilizo una busqueda por proximidad para encontrarlo en el arbol y modificar su nombre 
print("-----------------") 
print("Punto E")

# Buscamos por prefijo 'Dr' (proximidad)
pos = arbol_super.proximity_busqueda("Dr")
if pos is not None:
    print("Encontrado (por proximidad): ", pos.value)

    # elimino el nodo encontrado y insertamos con el nombre corregido
    deleted_value, deleted_other = arbol_super.delete(pos.value)
    
    if deleted_value is not None:
        arbol_super.insert("Doctor Strange", deleted_other)
        print("Nombre corregido a: Doctor Strange")
    else:
        print("No se pudo eliminar el nodo encontrado")

print("-----------------") 
print("Punto F")
arbol_super.in_order_des()

print("-----------------") 
print("Punto G")
arbol_h = BinaryTree() # arbol para superheroes
arbol_v = BinaryTree() # arbol para villanos 

arbol_super.divide_arbol(arbol_h, arbol_v) 
print("- Arbol de heroes:")
arbol_h.in_order()
print("-----------------")
print("- Arbol de villanos:")
arbol_v.in_order()
print("-----------------")

#  II. realizar un barrido ordenado alfabéticamente de cada árbol.
print("- Heroes ordenados alfabeticamente: ")
arbol_v.in_order()
print("-----------------")
print("- Villanos ordenados alfabeticamente: ")
arbol_v.in_order()
print("-----------------")

#I. determinar cuántos nodos tiene cada árbol;
print("- Determinar cuantos nodos hay en cada arbol")

hero = arbol_h.contar_heroes()
print(f"- Cantidad de Heroes: {hero}")
print("-----------------")
villan = arbol_v.contar_villain()
print(f'- Cantidad de Villanos: {villan}')