# 23. Dada una pila con los valores promedio de temperatura ambiente de cada día del mes de abril, obtener la siguiente información sin perder los datos:
#     a. determinar el rango de temperatura del mes, temperatura mínima y máxima;
#     b. calcular el promedio de temperatura (o media) del total de valores;
#     c. determinar la cantidad de valores por encima y por debajo de la media.

from ClasesPilas import Stack

lista_temp = [
    18.5, 19.0, 17.8, 20.1, 21.3, 22.0, 19.5, 18.9, 20.2, 21.1,
    20.4, 19.7, 18.3, 17.9, 19.6, 20.8, 21.5, 22.3, 23.0, 21.9,
    20.6, 19.8, 18.4, 17.5, 18.7, 19.9, 20.3, 21.0, 22.1, 21.7
]

pila_temp = Stack()

for temp in lista_temp:
    pila_temp.push(temp)

print("- Temperaturas del mes de abril - ")
pila_temp.show() # mostramos los elementos de la pila

print("-----------------------------------------")
print("- A. Rango de temperatura del mes -")

pila_aux_temp = Stack()
min = 1000
max = -1000
total = 0
cantidad = 0

while pila_temp.size() > 0:
    temp = pila_temp.pop()
    pila_aux_temp.push(temp)
    total += temp
    cantidad += 1
    if temp < min:
        min = temp
    if temp > max:
        max = temp
    pila_aux_temp.push(temp)

# Restaurar pila original
while pila_aux_temp.size() > 0:
    pila_temp.push(pila_aux_temp.pop())

print(f"[ Rando de temperatura: {max - min}°C ]")
print(f"[ Temperatura minima: {min}°C ] ")
print(f"[ Temperatura maxima: {max}°C ]")
print("-----------------------------------------")

# B. Promedio de temperatura

print("- B. Promedio del mes -")
promedio = (total / cantidad)
print(f"[ Promedio mensual: {promedio:.2f} °C ]")
print("-----------------------------------------")

# C. Cantidad por encima y por debajo de la media
print("- C. Valores por encima y por debajo del promedio -")
mayor = 0
menor = 0
pila_aux_temp2 = Stack()

while pila_temp.size() > 0:
    temp = pila_temp.pop()
    if temp > promedio:
        mayor += 1
    elif temp < promedio:
        menor += 1
    pila_aux_temp2.push(temp)

# Restaurar pila
while pila_aux_temp2.size() > 0:
    pila_temp.push(pila_aux_temp2.pop())

print(f"[ Días por encima del promedio: {mayor} ]")
print(f"[ Días por debajo del promedio: {menor} ]")
print("-------------------------------------------------------------------")
