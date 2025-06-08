#  17. Dado un párrafo que finaliza en punto, separar dicho párrafo en tres pilas: vocales, consonantes 
#      y otros caracteres que no sean letras (signos de puntuación números, espacios, etc.). Luego
#      utilizando las operaciones de pila resolver las siguientes consignas:
#     
#      a. cantidad de caracteres que hay de cada tipo (vocales, consonantes y otros);
# 
#      b. cantidad de espacios en blanco;
# 
#      c. porcentaje que representan las vocales respecto de las consonantes sobre el total de caracteres
#         del párrafo;
# 
#      d. cantidad de números;
# 
#      e. determinar si la cantidad de vocales y otros caracteres son iguales;
# 
#      f. determinar si existe al menos una z en la pila de consonantes.

from ClasesPilas import Stack

def separar_pilas(palabra):
    pila_vocales = Stack()
    pila_consonantes = Stack()
    pila_otros = Stack()

    for char in palabra:
        if char.isalpha():
            if char.lower() in 'aeiou':
                pila_vocales.push(char)
            else:
                pila_consonantes.push(char)
        elif char.isspace():
            continue  # Ignorar espacios en blanco
        else:
            pila_otros.push(char)

    return pila_vocales, pila_consonantes, pila_otros

def contar_caracteres(pila):
    contador = 0
    while not pila.is_empty():
        pila.pop()
        contador += 1
    return contador

def contar_espacios(pila): 
    contador = 0
    while not pila.is_empty():
        char = pila.pop()
        if char.isspace():
            contador += 1
    return contador

def porcentaje_vocales_consonantes(pila_vocales, pila_consonantes):
    total_vocales = contar_caracteres(pila_vocales)
    total_consonantes = contar_caracteres(pila_consonantes)
    total = total_vocales + total_consonantes

    if total == 0:
        return 0  # Evitar división por cero

    return (total_vocales / total) * 100, (total_consonantes / total) * 100

def contar_numeros(pila):
    contador = 0
    while not pila.is_empty():
        char = pila.pop()
        if char.isdigit():
            contador += 1
    return contador

def comparar_vocales_otros(pila_vocales, pila_otros):
    return contar_caracteres(pila_vocales) == contar_caracteres(pila_otros) 

def existe_z(pila_consonantes):
    while not pila_consonantes.is_empty():
        char = pila_consonantes.pop()
        if char.lower() == 'z':
            return True
    return False

# Ejemplo de uso
parrafo = "Hola, soy un ejemplo de párrafo con vocales, consonantes y otros caracteres 12345!"
