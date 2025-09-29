# Se cuenta con los vuelos del aeropuerto de Heraklion en Creta, de estos se sabe la siguiente
# información: empresa, número del vuelo, cantidad de asientos del avión, fecha de salida, destino,
# kms del vuelo. Y además se conoce los datos de cantidades de asientos totales y ocupados
# por clase (primera y turista). Implemente las funciones necesarias que permitan realizar las
# siguiente actividades:
# a. mostrar los vuelos con destino a Atenas, Miconos y Rodas;
# b. mostrar los vuelos con asientos clase turista disponible;
# c. mostrar el total recaudado por cada vuelo, considerando clase turista ($75 por kilómetro) y
# primera clase ($203 por kilómetro);
# d. mostrar los vuelos programados para una determinada fecha;
# e. vender un asiento (o pasaje) para un determinado vuelo;
# f. eliminar un vuelo. Tener en cuenta que si tiene pasajes vendidos, se debe indicar la cantidad
# de dinero a devovler;
# g. mostrar las empresas y los kilómetros de vuelos con destino a Tailandia.
from ClaseLista import List
from datetime import datetime

lista_vuelos = List()

vuelos = [
    # empresa, num_vuelo, asientos_totales, fecha_salida, destino, kms,
    # primera_total, primera_ocupados, turista_total, turista_ocupados
    ["Aegean", "A123", 180, "2024-06-10", "Atenas", 300, 20, 15, 160, 150],
    ["Olympic", "O456", 150, "2024-06-11", "Miconos", 250, 15, 10, 135, 130],
    ["SkyExpress", "S789", 200, "2024-06-12", "Rodas", 350, 30, 25, 170, 160],
    ["Aegean", "A321", 180, "2024-06-10", "Tailandia", 8000, 20, 18, 160, 150],
    ["Olympic", "O654", 150, "2024-06-13", "París", 2000, 15, 15, 135, 130],
    ["SkyExpress", "S987", 200, "2024-06-14", "Tailandia", 8000, 30, 28, 170, 165],
]

for vuelo in vuelos:
    lista_vuelos.append(vuelo)

# a. mostrar los vuelos con destino a Atenas, Miconos y Rodas;
def vuelo_destino(lista, destinos):
    resultado = List()
    for vuelo in lista:
        if vuelo[4] in destinos:
            resultado.append(vuelo)
    print(f"Vuelos con destino a {destinos}: ")
    for v in resultado:
        print(v)
    return resultado

# b. mostrar los vuelos con asientos clase turista disponible;
def vuelos_turista_dispo(lista):
    resultado = List()
    for vuelo in lista:
        turista_total = vuelo[8]
        turista_ocupados = vuelo[9]
        if turista_ocupados < turista_total:
            resultado.append(vuelo)
    print("Vuelos con asientos clase turista disponibles: ")
    for v in resultado:
        print(v)
    return resultado

# c. mostrar el total recaudado por cada vuelo, considerando clase turista ($75 por kilómetro) y
# primera clase ($203 por kilómetro);
def total_recaudado(lista):
    precio = {"turista": 75, "primera": 203}
    recaudaciones = []
    for vuelo in lista:
        kms = vuelo[5]
        primera_ocupados = vuelo[7]
        turista_ocupados = vuelo[9]
        total = primera_ocupados * precio["primera"] * kms + turista_ocupados * precio["turista"] * kms
        recaudaciones.append((vuelo[1],total))
    print("total recaudado por cada vuelo: ")
    for num, total in recaudaciones:
        print(f"Vuelo {num}: ${total}: ")
    return recaudaciones
# d. mostrar los vuelos programados para una determinada fecha;
def vuelos_por_fecha(lista, fecha_str):
    fecha = datetime.strptime(fecha_str, "%Y-%m-%d").date()
    resultado = List()
    for vuelo in lista:
        fecha_salida = datetime.strptime(vuelo[3], "%Y-%m-%d").date()
        if fecha_salida == fecha:
            resultado.append(vuelo)
    print(f"Vuelos programados para la fecha { fecha_str}:")
    for v in resultado:
        print(v)
    return resultado

# e. vender un asiento (o pasaje) para un determinado vuelo;
def vender_asiento(lista, num_vuelo, clase):
    for vuelo in lista:
        if vuelo[1] == num_vuelo:
            if clase == "primera":
                if vuelo[7] < vuelo[6]:
                    vuelo[7] += 1
                    print(f"Asiento de primera clase vendido en el vuelo {num_vuelo}")
                    return True
                else:
                    print(f"No hay asientos de primera clase disponibles en el vuelo {num_vuelo}")
                    return False
            elif clase == "turista":
                if vuelo[9] < vuelo[8]:
                    vuelo[9] += 1
                    print(f"Asientos de clase turista vendido en el vuelo {num_vuelo}")
                    return True
                else:
                    print(f"No hay asientos de primera clase disponibles en el vuelo {num_vuelo}")
                    return False    
            else:
                print("Clase no válida. Use 'primera' o 'turista'.")
                return False

    print(f"Vuelo {num_vuelo} no encontrado.")  
    return False

# f. eliminar un vuelo. Tener en cuenta que si tiene pasajes vendidos, se debe indicar la cantidad
# de dinero a devovler;
def eliminar_vuelo(lista,num_vuelo):
    precio = {"turista":75, "primera":203}
    for i, vuelo in enumerate(lista):
        if vuelo[1] == num_vuelo:
            primera_ocupados = vuelo[7]
            turista_ocupados = vuelo[9]
            kms = vuelo[5]
            total_vendido = primera_ocupados * precio["primera"] * kms + turista_ocupados * precio["turista"] * kms
            
            if primera_ocupados > 0 or turista_ocupados > 0:
                print(f"El vuelo {num_vuelo} tiene pasajes vendidos")
                print(f"Total a devolver: ${total_vendido}")
            else:
                print(f"El vuelo {num_vuelo} no tiene pasajes vendidos")
            lista.pop(i)
            print(f"Vuelo {num_vuelo} eliminado.")
            return True
        
    print(f"Vuelo {num_vuelo} no encontrado")
    return False

# g. mostrar las empresas y los kilómetros de vuelos con destino a Tailandia.
def empresa_kms_tailandia(lista):
    resultado = list()
    for vuelo in lista:
        if vuelo[4] == "tailandia":
            empresa = vuelo[0]
            kms = vuelo[5]
            if empresa in resultado:
                resultado[empresa] += kms
            else:
                resultado[empresa] = kms

    print("empresas y kilometros de vuelos con destinos a tailandia")
    for empresa, kms in resultado.items():
        print(f"empresa: {empresa}, kms: {kms}")

#prueba
vuelo_destino(lista_vuelos, ["Atenas", "Miconos", "Rodas"])
vuelos_turista_dispo(lista_vuelos)
total_recaudado(lista_vuelos)
vuelos_por_fecha(lista_vuelos, "2024-06-10")
vender_asiento(lista_vuelos, "A123", "turista")
eliminar_vuelo(lista_vuelos, "O456")
empresa_kms_tailandia(lista_vuelos)