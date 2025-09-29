# 11. Dada una lista que contiene información de los personajes de la saga de Star Wars con la siguiente
#     información nombre, altura, edad, género, especie, planeta natal y episodios en los que
#     apareció, desarrollar los algoritmos que permitan realizar las siguientes actividades:
#       
#       a. listar todos los personajes de género femenino;
#       
#       b. listar todos los personajes de especie Droide que aparecieron en los primeros seis episodios
#       de la saga;
#       
#       c. mostrar toda la información de Darth Vader y Han Solo;
#       
#       d. listar los personajes que aparecen en el episodio VII y en los tres anteriores;
#       
#       e. mostrar los personajes con edad mayor a 850 años y de ellos el mayor;
#       
#       f. eliminar todos los personajes que solamente aparecieron en los episodios IV, V y VI;
#       
#       g. listar los personajes de especie humana cuyo planeta de origen es Alderaan;
#       
#       h. mostrar toda la información de los personajes cuya altura es menor a 70 centímetros;
#       
#       i. determinar en qué episodios aparece Chewbacca y mostrar además toda su información.

from ClaseLista import List

lista_personajes = List([
    {
        "nombre": "Leia Organa",
        "altura": 150,
        "edad": 19,
        "genero": "femenino",
        "especie": "humano",
        "planeta": "Alderaan",
        "episodios": ["IV", "V", "VI", "VII", "VIII"]
    },
    {
        "nombre": "Luke Skywalker",
        "altura": 172,
        "edad": 23,
        "genero": "masculino",
        "especie": "humano",
        "planeta": "Tatooine",
        "episodios": ["IV", "V", "VI", "VII", "VIII"]
    },
    {
        "nombre": "Darth Vader",
        "altura": 202,
        "edad": 45,
        "genero": "masculino",
        "especie": "humano",
        "planeta": "Tatooine",
        "episodios": ["III", "IV", "V", "VI"]
    },
    {
        "nombre": "Han Solo",
        "altura": 180,
        "edad": 32,
        "genero": "masculino",
        "especie": "humano",
        "planeta": "Corellia",
        "episodios": ["IV", "V", "VI", "VII"]
    },
    {
        "nombre": "Padme Amidala",
        "altura": 165,
        "edad": 27,
        "genero": "femenino",
        "especie": "humano",
        "planeta": "Naboo",
        "episodios": ["I", "II", "III"]
    },
    {
        "nombre": "C-3PO",
        "altura": 167,
        "edad": 112,
        "genero": "ninguno",
        "especie": "droide",
        "planeta": "Desconocido",
        "episodios": ["I", "II", "III", "IV", "V", "VI", "VII", "VIII"]
    },
    {
        "nombre": "R2-D2",
        "altura": 96,
        "edad": 66,
        "genero": "ninguno",
        "especie": "droide",
        "planeta": "Naboo",
        "episodios": ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
    },
    {
        "nombre": "Yoda",
        "altura": 66,
        "edad": 900,
        "genero": "masculino",
        "especie": "desconocida",
        "planeta": "Desconocido",
        "episodios": ["I", "II", "III", "V", "VI", "VIII"]
    },
    {
        "nombre": "Chewbacca",
        "altura": 228,
        "edad": 200,
        "genero": "masculino",
        "especie": "wookiee",
        "planeta": "Kashyyyk",
        "episodios": ["III", "IV", "V", "VI", "VII", "VIII", "IX"]
    },
    {
        "nombre": "Rey",
        "altura": 170,
        "edad": 19,
        "genero": "femenino",
        "especie": "humano",
        "planeta": "Jakku",
        "episodios": ["VII", "VIII", "IX"]
    },
    {
        "nombre": "Obi-Wan Kenobi",
        "altura": 182,
        "edad": 57,
        "genero": "masculino",
        "especie": "humano",
        "planeta": "Stewjon",
        "episodios": ["I", "II", "III", "IV"]
    },
    {
        "nombre": "Bail Organa",
        "altura": 185,
        "edad": 52,
        "genero": "masculino",
        "especie": "humano",
        "planeta": "Alderaan",
        "episodios": ["II", "III"]
    },
    {
        "nombre": "BB-8",
        "altura": 67,
        "edad": 2,
        "genero": "ninguno",
        "especie": "droide",
        "planeta": "Desconocido",
        "episodios": ["VII", "VIII", "IX"]
    }
])

#a. listar todos los personajes de género femenino;
print("- Punto A -")   

p_femenino = [p for p in lista_personajes if p["genero"] == "femenino"]

print("- Personajes de genero femenino")

for p in p_femenino:
    print(p["nombre"])

print("---------------------------")

#b. listar todos los personajes de especie Droide que aparecieron en los primeros seis episodios de la saga;
print("- Punto B -")   

episodios = {"I","II","III","IV","V","VI"}

droides_episodios = [
    p for p in lista_personajes
    if p["especie"] == "droide" and episodios.intersection(p["episodios"])
]

print("- Droides que aparecieron en los episodios del I al VI")
for p in droides_episodios:
    print(p["nombre"])

print("----------------------------")
#c. mostrar toda la información de Darth Vader y Han Solo;
print("- Punto C -")
nombre_buscado = {"Darth Vader", "Han Solo"}

personaje_buscado = [p for p in lista_personajes if p["nombre"] in nombre_buscado]

print("- Informacion de Darth Vader y Han Solo")
for p in personaje_buscado:
    print(p)

print("-----------------------------")
#d. listar los personajes que aparecen en el episodio VII y en los tres anteriores;
print("- Punto D -")

episodios_previos = {"IV","V","VI"}

personajes_episodios = [
    p for p in lista_personajes
    if "VII" in p["episodios"] and episodios_previos.issubset(set(p["episodios"]))
]

print("- Personajes que aparecen en el Episodio VII y en los tres anterioses")
for p in personajes_episodios:
    print(p["nombre"])

print("----------------------------")
#e. mostrar los personajes con edad mayor a 850 años y de ellos el mayor;
print("- Punto E -")
ancianos = [p for p in lista_personajes if p["edad"] > 850]

print("- Personajes con edad mayor a 850 anios -")
for p in ancianos:
    print(f"- {p["nombre"]} - {p["edad"]} anio")

if ancianos:
    mas_viejos = max(ancianos, key = lambda p: p["edad"])
    print("\n- El personaje mas viejo es: ")
    print(f"- {mas_viejos["nombre"]} - {mas_viejos["edad"]} anios")
else:
    print("- No hay personajes mayores a 850 anios")

print("-----------------------------")
#f. eliminar todos los personajes que solamente aparecieron en los episodios IV, V y VI;
print("- Punto F -")

episodios_clasicos = {"IV","V","VI"}

personajes_filtrados = [
    p for p in lista_personajes 
    if set(p["episodios"]) != episodios_clasicos
]

print("- Lista de personajes de elimnar los que solo aparecen en IV, V y VI")
for p in personajes_filtrados:
    print(p["nombre"])

print("-------------------------------")
#g. listar los personajes de especie humana cuyo planeta de origen es Alderaan;
print("- Punto G -")

humanos_alderaan = [
    p for p in lista_personajes if p["especie"] == "humano" and p["planeta"] == "Alderaan"
]

print("- Humanos originales de Alderaan")
for p in humanos_alderaan:
    print(p["nombre"])

print("------------------------------")
#h. mostrar toda la información de los personajes cuya altura es menor a 70 centímetros;
print("- Punto H -")

personajes_bajos = [p for p in lista_personajes if p["altura"] < 70]

print("- Personajes con altura menores a 70cm -")
for p in personajes_bajos:
    print(p)

print("-------------------------------")
#i. determinar en qué episodios aparece Chewbacca y mostrar además toda su información
print("- Punto I -")

personajes_info = next((p for p in lista_personajes if p["nombre"] == "Chewbacca"), None)

if personajes_info:
    print("- Informacion completa de Chewbacca")
    print(personajes_info)
    print("\nEpisodios en los que aparece:")
    print(", ".join(personajes_info["episodios"]))
else:
    print("Chewbacca no está en la lista.")