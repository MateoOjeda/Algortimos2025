# # 9. Se tiene una lista de los alumnos de un curso, de los que se sabe nombre, apellido y legajo.
#      Por otro lado se tienen las notas de los diferentes parciales que rindió cada uno de ellos con
#      la siguiente información: materia que rindió, nota obtenida y fecha de parcial. Desarrollar un
#      algoritmo que permita realizar la siguientes actividades:
#      
#      a. mostrar los alumnos ordenados alfabéticamente por apellido;
#      
#      b. indicar los alumnos que no desaprobaron ningún parcial;
#      
#      c. determinar los alumnos que tienen promedio mayor a 8,89;
#      
#      d. mostrar toda la información de los alumnos cuyos apellidos comienzan con L;
#      
#      e. mostrar el promedio de cada uno de los alumnos;
#      
#      f. mostrar todos los alumnos que rindieron la cátedra “Algoritmos y estructuras de datos”;
#      
#      g. indicar el porcentaje de parciales aprobados de un alumno indicado por el usuario;
#      
#      h. indicar cuantos alumnos aprobaron y desaprobaron parciales de la cátedra “Base de datos”;
#      
#      i. mostrar todos los alumnos que rindieron en el año 2020;
#      
#      j. debe modificar el TDA para implementar lista de lista

from ClaseLista import List

lista_alumnos = List([
    {'nombre': 'Diego', 'apellido': 'Martinez', 'legajo': 1000},
    {'nombre': 'Sofia', 'apellido': 'Fernandez', 'legajo': 1001},
    {'nombre': 'Juan', 'apellido': 'Romero', 'legajo': 1002},
    {'nombre': 'Maria', 'apellido': 'Gomez', 'legajo': 1003},
    {'nombre': 'Diego', 'apellido': 'Sanchez', 'legajo': 1004},
    {'nombre': 'Martin', 'apellido': 'Torres', 'legajo': 1005},
    {'nombre': 'Juan', 'apellido': 'Martinez', 'legajo': 1006},
    {'nombre': 'Juan', 'apellido': 'Martinez', 'legajo': 1007},
    {'nombre': 'Lucia', 'apellido': 'Fernandez', 'legajo': 1008},
    {'nombre': 'Maria', 'apellido': 'Torres', 'legajo': 1009},
    
])
lista_notas = List([
    {'legajo': 1000, 'materia': 'Quimica', 'nota': 9, 'fecha': '2020-03-08'},
    {'legajo': 1000, 'materia': 'Biologia', 'nota': 6, 'fecha': '2020-03-22'},
    {'legajo': 1001, 'materia': 'Fisica', 'nota': 10, 'fecha': '2020-05-03'},
    {'legajo': 1001, 'materia': 'Quimica', 'nota': 6, 'fecha': '2020-05-14'},
    {'legajo': 1001, 'materia': 'Ingles', 'nota': 5, 'fecha': '2020-03-17'},
    {'legajo': 1001, 'materia': 'Matematica', 'nota': 3, 'fecha': '2020-04-30'},
    {'legajo': 1001, 'materia': 'Biologia', 'nota': 5, 'fecha': '2020-05-13'},
    {'legajo': 1002, 'materia': 'Quimica', 'nota': 10, 'fecha': '2020-03-21'},
    {'legajo': 1002, 'materia': 'Geografia', 'nota': 4, 'fecha': '2020-04-23'},
    {'legajo': 1003, 'materia': 'Quimica', 'nota': 8, 'fecha': '2020-04-14'},
    {'legajo': 1003, 'materia': 'Ingles', 'nota': 8, 'fecha': '2020-03-10'},
    {'legajo': 1003, 'materia': 'Matematica', 'nota': 6, 'fecha': '2024-05-07'},
    {'legajo': 1003, 'materia': 'Geografia', 'nota': 4, 'fecha': '2024-03-29'},
    {'legajo': 1004, 'materia': 'Fisica', 'nota': 1, 'fecha': '2024-03-06'},
    {'legajo': 1004, 'materia': 'Biologia', 'nota': 6, 'fecha': '2024-05-24'},
    {'legajo': 1004, 'materia': 'Matematica', 'nota': 5, 'fecha': '2024-05-11'},
    {'legajo': 1004, 'materia': 'Historia', 'nota': 5, 'fecha': '2024-03-04'},
    {'legajo': 1004, 'materia': 'Fisica', 'nota': 8, 'fecha': '2024-03-03'},
    {'legajo': 1005, 'materia': 'Geografia', 'nota': 9, 'fecha': '2024-03-07'},
    {'legajo': 1005, 'materia': 'Quimica', 'nota': 8, 'fecha': '2024-03-07'},
    {'legajo': 1005, 'materia': 'Matematica', 'nota': 4, 'fecha': '2024-03-08'},
    {'legajo': 1005, 'materia': 'Biologia', 'nota': 2, 'fecha': '2024-04-08'},
    {'legajo': 1005, 'materia': 'Matematica', 'nota': 5, 'fecha': '2024-04-02'},
    {'legajo': 1006, 'materia': 'Fisica', 'nota': 4, 'fecha': '2024-05-11'},
    {'legajo': 1006, 'materia': 'Biologia', 'nota': 3, 'fecha': '2024-04-21'},
    {'legajo': 1006, 'materia': 'Ingles', 'nota': 5, 'fecha': '2024-04-01'},
    {'legajo': 1006, 'materia': 'Matematica', 'nota': 5, 'fecha': '2024-03-19'},
    {'legajo': 1007, 'materia': 'Ingles', 'nota': 6, 'fecha': '2024-05-07'},
    {'legajo': 1007, 'materia': 'Fisica', 'nota': 4, 'fecha': '2024-03-30'},
    {'legajo': 1007, 'materia': 'Lengua', 'nota': 1, 'fecha': '2024-03-18'},
    {'legajo': 1007, 'materia': 'Quimica', 'nota': 5, 'fecha': '2024-05-03'},
    {'legajo': 1008, 'materia': 'Lengua', 'nota': 4, 'fecha': '2024-04-19'},
    {'legajo': 1008, 'materia': 'Matematica', 'nota': 7, 'fecha': '2024-03-04'},
    {'legajo': 1008, 'materia': 'Geografia', 'nota': 6, 'fecha': '2024-04-10'},
    {'legajo': 1008, 'materia': 'Biologia', 'nota': 1, 'fecha': '2024-03-20'},
    {'legajo': 1009, 'materia': 'Ingles', 'nota': 2, 'fecha': '2024-03-30'},
    {'legajo': 1009, 'materia': 'Historia', 'nota': 9, 'fecha': '2024-03-31'},
])

#a. mostrar los alumnos ordenados alfabéticamente por apellido;
print("- Punto A - Alumnos ordenados alfabeticamente por apellido:")
alumnos = lista_alumnos.add_criterion("apellido", lambda alumno: alumno["apellido"])# Acceder a los elementos de la lista de alumnos

#ordenar usando ese criterio
lista_alumnos.sort_by_criterion("apellido")

lista_alumnos.show()

print("-----------------------------------------------------------")
#b. indicar los alumnos que no desaprobaron ningún parcial;
print("- Punto B - ")
notas_por_legajo = {}

for nota in lista_notas:
    legajo = nota["legajo"]
    if legajo not in notas_por_legajo:
        notas_por_legajo[legajo] = []
    notas_por_legajo[legajo].append(nota["nota"])

# Recorrer lista de alumnos y mostrar los qe no desaporbaron
print("- Alumnos que no desaprobaron ningun parcial -")
for alumno in lista_alumnos:
    legajo = alumno["legajo"]
    notas = notas_por_legajo.get(legajo, [])
    
    # Consideramos que no desaprobó si TODAS las notas son >= 6
    if all(n >= 6 for n in notas) and notas:
        print(f"- {alumno["nombre"]},  {alumno["apellido"]} (Legajo: {legajo})")


print("-----------------------------------------------------------")  

#c. determinar los alumnos que tienen promedio mayor a 8,89;
print("- Punto C - Alumnos con promedio mayor a 8.89")

for alumno in lista_alumnos:
    legajo = alumno["legajo"]
    notas= notas_por_legajo.get(legajo,[])

    if notas:
        promedio = sum(notas) / len(notas)
        if promedio >= 6:
            print(f"- {alumno["nombre"]}, {alumno["apellido"]} (Legajo: {legajo}) -Promedio: {promedio}")
print("-----------------------------------------------------------")   

#d. mostrar toda la información de los alumnos cuyos apellidos comienzan con L;
print("- Punto D - Alumnos con apellido que comienza con 'L' ")

lista_alumnos.append({'nombre': 'Laura', 'apellido': 'Lopez', 'legajo': 1010})


for alumno in lista_alumnos:
    if alumno["apellido"].startswith("L"):
        print(alumno)

print("-----------------------------------------------------------")   

#e. mostrar el promedio de cada uno de los alumnos;
print("- Punto E - Promedio de todos los estudiantes -")

for alumno in lista_alumnos:
    legajo = alumno["legajo"]
    notas= notas_por_legajo.get(legajo,[])

    if notas:
        promedio = sum(notas) / len(notas)
        print(f"- {alumno["nombre"]}, {alumno["apellido"]} (Legajo: {legajo}) -Promedio: {promedio}")
    else:
        print(f"- {alumno["nombre"]} {alumno["apellido"]} (legajo: {legajo}) - Sin Parcial")

print("-----------------------------------------------------------")      
#f. mostrar todos los alumnos que rindieron la cátedra “Algoritmos y estructuras de datos”;
print("- Punto F - Alumnos que rindieron Matematica")

#conjunto de legajos que rindieron esa materia
legajo_matematicas = set()

for nota in lista_notas:
    if nota["materia"].lower() in ["matematica"]:
        legajo_matematicas.add(nota["legajo"])

# buscar los alumnos con esos legajos
for alumno in lista_alumnos:
    if alumno["legajo"] in legajo_matematicas:
        print(f"- {alumno["nombre"]} {alumno["apellido"]} (Legajo: {alumno["legajo"]})")

print("-----------------------------------------------------------")     
#g. indicar el porcentaje de parciales aprobados de un alumno indicado por el usuario;
print("- Punto G - Parciales aprobados")

legajo_input = int(input("ingrese numero de legajo del alumno: "))

#buscar notas por legajo
notas = notas_por_legajo.get(legajo_input, [])

if notas:
    total = len(notas)
    aprobados = sum(1 for n in notas if n >= 6)
    porcentaje = (aprobados / total) / 100
    print(f"- El alumno con legajo {legajo_input} aprobo el {porcentaje}% de sus materias")

print("-----------------------------------------------------------")      

#h. indicar cuantos alumnos aprobaron y desaprobaron parciales de la cátedra “Base de datos”;
print("- Punto H - Parciales de la catedra Biologia")

aprobados = set()
desaprobados = set()

for nota in lista_notas:
    if nota["materia"].lower() == "biologia":
        legajo = nota["legajo"]
        if nota["nota"] >= 6:
            aprobados.add(legajo)
        else:
            desaprobados.add(legajo)

#evitaos contar dos veces los que aprobamos
solo_desaprobados = desaprobados - aprobados

print(f"- Alumnos que aprobaros los parciales de Biologia: {len(aprobados)}")
print(f"- Alumnos que desaprobaros los parciales de Biologia: {len(desaprobados)}")

print("-----------------------------------------------------------") 

#i. mostrar todos los alumnos que rindieron en el año 2020;
print("- Punto I - Alumnos que rindieron en el anio 2020")

legajo_2020 = set()

for nota in lista_notas:
    if nota["fecha"].startswith("2020"):
        legajo_2020.add(nota["legajo"])

for alumno in lista_alumnos:
    if alumno["legajo"] in legajo_2020:
        print(f"- {alumno["nombre"]} {alumno["apellido"]} (Legajo: {alumno["legajo"]})")

print("-----------------------------------------------------------")  

#j. debe modificar el TDA para implementar lista de lis
print("- Punto J - ")

print("-----------------------------------------------------------")


