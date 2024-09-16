import random

# Parámetros
num_ciudades = 3
num_dias_semana = 7
num_semanas = 4

# Generar matriz 3D de temperaturas aleatorias
def generar_temperaturas(num_ciudades, num_dias_semana, num_semanas):
    temperaturas = [[[random.randint(15, 30) for _ in range(num_dias_semana)] for _ in range(num_semanas)] for _ in range(num_ciudades)]
    return temperaturas

# Crear la matriz de temperaturas
temperaturas = generar_temperaturas(num_ciudades, num_dias_semana, num_semanas)

print("Matriz de temperaturas (Ciudades x Días x Semanas):")
for ciudad in range(num_ciudades):
    for semana in range(num_semanas):
        print(f"Ciudad {ciudad+1}, Semana {semana+1}: {temperaturas[ciudad][semana]}")

# Calcular el promedio de temperaturas para cada ciudad y semana
def calcular_promedios(temperaturas):
    promedios = [[0] * num_semanas for _ in range(num_ciudades)]
    for ciudad in range(num_ciudades):
        for semana in range(num_semanas):
            semana_temperaturas = temperaturas[ciudad][semana]
            promedio = sum(semana_temperaturas) / len(semana_temperaturas)
            promedios[ciudad][semana] = promedio
    return promedios

# Obtener los promedios
promedios = calcular_promedios(temperaturas)

# Mostrar los promedios
print("\nPromedio de temperaturas por ciudad y semana:")
for ciudad in range(num_ciudades):
    for semana in range(num_semanas):
        print(f"Ciudad {ciudad+1}, Semana {semana+1}: {promedios[ciudad][semana]:.2f} °C")
