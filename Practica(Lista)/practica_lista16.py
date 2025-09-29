# Se deben administrar las actividades de un proyecto de software, de estas se conoce su costo,
# tiempo de ejecución, fecha de inicio, fecha de fin estimada, fecha de fin efectiva y persona a
# cargo. Desarrollar un algoritmo que realice las siguientes actividades:
# a. tiempo promedio de tareas;
# b. costo total del proyecto;
# c. actividades realizadas por una determinada persona;
# d. mostrar la información de las tareas a realizar entre dos fechas dadas;
# e. mostrar las tareas finalizadas en tiempo y las finalizadas fuera de tiempo;
# f. indicar cuántas tareas le quedan pendientes a una determinada persona, indicada por
# el usuario.
from ClaseLista import List
from datetime import datetime

lista_actividades = List()

actividades = [
    # Actividad 1: Finalizada en tiempo, Juan
    ["Diseño de UI", 5000.0, 10, "2023-10-01", "2023-10-11", "2023-10-10", "Juan"],
    # Actividad 2: Finalizada fuera de tiempo, María
    ["Desarrollo Backend", 10000.0, 20, "2023-10-12", "2023-11-01", "2023-11-05", "María"],
    # Actividad 3: Pendiente, Pedro
    ["Pruebas Unitarias", 3000.0, 5, "2023-11-02", "2023-11-07", None, "Pedro"],
    # Actividad 4: Finalizada en tiempo, Ana
    ["Integración API", 7000.0, 15, "2023-11-08", "2023-11-23", "2023-11-22", "Ana"],
    # Actividad 5: Finalizada fuera de tiempo, Juan
    ["Desarrollo Frontend", 8000.0, 12, "2023-11-24", "2023-12-06", "2023-12-10", "Juan"],
    # Actividad 6: Pendiente, María
    ["Optimización de Base de Datos", 4000.0, 8, "2023-12-07", "2023-12-15", None, "María"],
    # Actividad 7: Finalizada en tiempo, Pedro
    ["Documentación del Código", 2000.0, 7, "2023-10-05", "2023-10-12", "2023-10-11", "Pedro"],
    # Actividad 8: Finalizada fuera de tiempo, Ana
    ["Pruebas de Seguridad", 6000.0, 10, "2023-12-16", "2023-12-26", "2023-12-30", "Ana"],
    # Actividad 9: Pendiente, Juan
    ["Despliegue en Producción", 9000.0, 5, "2024-01-01", "2024-01-06", None, "Juan"],
    # Actividad 10: Finalizada en tiempo, Luis (nueva persona)
    ["Revisión Final", 1500.0, 3, "2023-10-15", "2023-10-18", "2023-10-17", "Luis"]
]

for actividades in lista_actividades:
    lista_actividades.insert(actividades)

# a. tiempo promedio de tareas;
def tiempo_promedio(actividades):

    if not actividades:
        return 0.0
    tiempo_suma = sum(actividad[2] for actividad in actividades)
    
    return tiempo_suma / len(actividades)

tiempo_promedio(actividades)     

# b. costo total del proyecto;
def costo_total(actividades):

    if not actividades:
        return 0.0
    return sum(actividad[1] for actividad in actividades)
    
costo_total(actividades)

# c. actividades realizadas por una determinada persona;
def actividades_personas(actividades, nombre_persona):
    resultado = []
    for actividad in actividades:
        if actividad[6].lower() == nombre_persona.lower():
            resultado.append(actividad[0])
    if resultado:
        print(f"Actividades de {nombre_persona}: {resultado}")
        return resultado
    else: 
        print(f"No se enccontraron actividades para {nombre_persona}")
        return 0
    

# d. mostrar la información de las tareas a realizar entre dos fechas dadas;
def tarea_entre_fechas(actividades, fecha_inicial_str, fecha_final_str):
    fecha_inicial = datetime.strptime(fecha_inicial_str, "%Y-%m-%d")
    fecha_final = datetime.strptime(fecha_final_str, "%Y-%m-%d")
    resultado = []
    for actividad in actividades:
        #Convertir fechas de la actividad a date
        f_inicio = datetime.strptime(actividad[3], "%Y-%m-%d")
        f_fin_estimado = datetime.strptime(actividad[4], "%Y-%m-%d")

        #Considero tareas que estan programadas para realizar entre las fechas
        if (fecha_inicial <= f_inicio <= fecha_final) or (fecha_inicial <= f_fin_estimado <= fecha_final):
            resultado.append(actividad)
    
    if resultado:
        print(f"Tareas entre {fecha_inicial_str} y {fecha_final_str}:")
        for act in resultado:
            print(act)
    else:
        print(f"No se encontro la fecha")
    return resultado
# e. mostrar las tareas finalizadas en tiempo y las finalizadas fuera de tiempo;
def tarea_finalizadas(actividades):
    en_tiempo = []
    fuera_tiempo = []

    for acitvidad in actividades:
        fecha_fin_efectividad = acitvidad[5]
        if fecha_fin_efectividad is not None:
            fecha_fin_efectiva = datetime_strptime(fecha_fin_efectiva, "%Y-%m-%d")
            fecha_fin_estimado = datetime.strptime(acitvidad[4], "%Y-%m-%d")
            if fecha_fin_efectiva <= fecha_fin_estimado:
                en_tiempo.append(actividad)
            else:
                fuera_tiempo.append(acitvidad)
    print("Tareas finalizadas en tiempo:")
    for act in en_tiempo:
        print(act)
    print("Tareas finalizadas fuera de tiempo:")
    for act in fuera_tiempo:
        print(act)
    return en_tiempo, fuera_tiempo

# f. indicar cuántas tareas le quedan pendientes a una determinada persona, indicada por el usuario.
def tareas_pendientes_personas(actividades, nombre_persona):
    pendientes = 0
    for actividad in actividades:
        if actividad[6].lower() == nombre_persona.lower() and actividad[5] in None:
            pendientes += 1
    print(f"Tareas pendienstes de {nombre_persona}: {pendientes}")
    return pendientes


# Ejemplo--
print("a) Tiempo promedio de tareas:", tiempo_promedio(lista_actividades))
print("b) Costo total del proyecto:", costo_total(lista_actividades))
actividades_personas(lista_actividades, "Juan")
tarea_entre_fechas(lista_actividades, "2023-11-01", "2023-12-01")
tarea_finalizadas(lista_actividades)
tareas_pendientes_personas(lista_actividades, "María")