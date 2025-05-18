# 1.- Actualizar valores en diccionarios y listas

matriz = [ [10, 15, 20], [3, 7, 14] ]
cantantes = [
    {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
    {"nombre": "Chayanne", "pais": "Puerto Rico"}
]

ciudades = {
    "México": ["Ciudad de México", "Guadalajara", "Cancún"],
    "Chile": ["Santiago", "Concepción", "Viña del Mar"]
}

coordenadas = [
    {"latitud": 8.2588997, "longitud": -84.9399704}
]

# a) 
matriz[1][0] = 6
matriz

# b)
cantantes[0]['nombre'] = 'Enrique Martin Morales'
cantantes[0]['nombre']

# c)
ciudades['México'][2] = 'Monterrey'
ciudades['México'][2]

# d)
coordenadas[0]['latitud'] = 9.9355431
coordenadas[0]['latitud']

# 2.- Iterar a través de una lista de diccionarios
cantantes = [
    {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
    {"nombre": "Chayanne", "pais": "Puerto Rico"},
    {"nombre": "José José", "pais": "México"},
    {"nombre": "Juan Luis Guerra", "pais": "República Dominicana"}
]

def iterarDiccionario(lista):
    for diccionario in lista:
        for llave, valor in diccionario.items():
            print(f"{llave}: {valor}")

iterarDiccionario(cantantes)

# 3.- Obtener valores de una lista de diccionarios
def iterarDiccionario2(llave, lista):
    for diccionario in lista:
        if llave in diccionario:
            print(diccionario[llave])
        else:
            print(f"La llave '{llave}' no se encuentra en el diccionario.")

iterarDiccionario2('nombre', cantantes)
iterarDiccionario2('pais', cantantes)

# 4.- Iterar a través de un diccionario con valores de lista
costa_rica = {
    "ciudades": ["San José", "Limón", "Cartago", "Puntarenas"],
    "comidas": ["gallo pinto", "casado", "tamales", "chifrijo", "olla de carne"]
}

def imprimirInformacion(diccionario):
    print('Diccionario contiene {} listas'.format(len(diccionario)))
    for llave, valores in diccionario.items():
        print(f"{len(valores)} {llave.upper()}")
        for valor in valores:
            print(f"{valor}")
        print()  # Línea en blanco para separar las secciones

imprimirInformacion(costa_rica)