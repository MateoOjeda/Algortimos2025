# 10. Se dispone de una lista de canciones de Spotify, de las cuales se sabe su nombre, banda o artista,
#     duración y cantidad de reproducciones durante el último mes. Desarrollar un algoritmo que
#     permita realizar las siguientes actividades:
# 
#         a. obtener la información de la canción más larga;
# 
#         b. obtener el TOP 5, TOP 10 y TOP 40 de canciones más escuchadas;
# 
#         c. obtener todas las canciones de la banda Arctic Monkeys;
# 
#         d. mostrar los nombres de las bandas o artistas que solo son de una palabra.

from ClaseLista import List

lista_canciones = List([
    {"nombre": "Do I Wanna Know?", "banda": "Arctic Monkeys", "duracion": 272, "reproducciones": 1500000},
    {"nombre": "Bohemian Rhapsody", "banda": "Queen", "duracion": 354, "reproducciones": 2000000},
    {"nombre": "Blinding Lights", "banda": "The Weeknd", "duracion": 200, "reproducciones": 2200000},
    {"nombre": "R U Mine?", "banda": "Arctic Monkeys", "duracion": 202, "reproducciones": 1100000},
    {"nombre": "One Dance", "banda": "Drake", "duracion": 173, "reproducciones": 1900000},
    {"nombre": "Believer", "banda": "Imagine Dragons", "duracion": 204, "reproducciones": 1750000},
    {"nombre": "Shape of You", "banda": "Ed Sheeran", "duracion": 233, "reproducciones": 2300000},
    {"nombre": "Sweater Weather", "banda": "The Neighbourhood", "duracion": 240, "reproducciones": 1250000},
    {"nombre": "505", "banda": "Arctic Monkeys", "duracion": 268, "reproducciones": 1300000},
    {"nombre": "Levitating", "banda": "Dua Lipa", "duracion": 203, "reproducciones": 1400000},
    {"nombre": "Peaches", "banda": "Justin Bieber", "duracion": 198, "reproducciones": 1150000},
    {"nombre": "Bad Habits", "banda": "Ed Sheeran", "duracion": 231, "reproducciones": 1600000},
    {"nombre": "Radioactive", "banda": "Imagine Dragons", "duracion": 186, "reproducciones": 1000000},
    {"nombre": "Money Trees", "banda": "Kendrick Lamar", "duracion": 376, "reproducciones": 900000},
    {"nombre": "Lonely", "banda": "Akon", "duracion": 238, "reproducciones": 800000},
    {"nombre": "Happier", "banda": "Marshmello", "duracion": 214, "reproducciones": 950000},
    {"nombre": "Stolen Dance", "banda": "Milky Chance", "duracion": 300, "reproducciones": 700000},
    {"nombre": "Lucid Dreams", "banda": "Juice WRLD", "duracion": 239, "reproducciones": 1700000},
    {"nombre": "Numb", "banda": "Linkin Park", "duracion": 185, "reproducciones": 2100000},
    {"nombre": "Uptown Funk", "banda": "Bruno Mars", "duracion": 270, "reproducciones": 1950000}
])

#a. obtener la información de la canción más larga;
print("- Punto A -")

canciones_mas_larga = max(lista_canciones, key = lambda c: c["duracion"])
print(f"- La cancion mas larga es: {canciones_mas_larga}")

print("-----------------------------------")

#b. obtener el TOP 5, TOP 10 y TOP 40 de canciones más escuchadas;
print("- Punto B -")

canciones_odenadas = sorted(lista_canciones, key=lambda c: c["reproducciones"], reverse=True)

top_5 = canciones_odenadas[:5]
top_10 = canciones_odenadas[:10]
top_40 = canciones_odenadas[:40] # si tenemos menos de 40 devuelve todas las canciones

print("- Top 5 Canciones mas Escuchadas -")
for c in top_5:
    print(f" {c["nombre"]} - {c["banda"]} ({c["reproducciones"]}) reproducciones")
print("|||||||||||||||||||||||||||||||||||||||||||||||||||")

print("- Top 10 Canciones mas Escuchadas -")
for c in top_10:
    print(f" {c["nombre"]} - {c["banda"]} ({c["reproducciones"]}) reproducciones")
print("|||||||||||||||||||||||||||||||||||||||||||||||||||")
 
print("- Top 40 Canciones mas Escuchadas -")
for c in top_40:
    print(f" {c["nombre"]} - {c["banda"]} ({c["reproducciones"]}) reproducciones")
print("|||||||||||||||||||||||||||||||||||||||||||||||||||")

print("-----------------------------------")

#c. obtener todas las canciones de la banda Arctic Monkeys;
print("- Punto C -")

canciones_artic = [c for c in lista_canciones if c["banda"] == "Arctic Monkeys"]
print("- Caciones de Arctic Monkeys")
for c in lista_canciones:
    print(f"- {c["nombre"]} ({c["duracion"]}) seg, {c["reproducciones"]} reproducciones")

print("-----------------------------------")

#d. mostrar los nombres de las bandas o artistas que solo son de una palabra.
print("- Punto D -")

bandas_unapalabra = set(c["banda"] for c in lista_canciones if len(c["banda"].split()) == 1 ) 

print("- Bandas o Artistas de una sola palabra")
for banda in bandas_unapalabra:
    print(banda)
print("-----------------------------------")
