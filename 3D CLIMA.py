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
import random

# Parámetros
num_ciudades = 3
num_dias_semana = 7
num_semanas = 4


# Generar matriz 3D de temperaturas aleatorias
def generar_temperaturas(num_ciudades, num_dias_semana, num_semanas):
    """
    Genera una matriz 3D de temperaturas aleatorias para múltiples ciudades,
    días de la semana y semanas.

    :param num_ciudades: Número de ciudades
    :param num_dias_semana: Número de días en una semana
    :param num_semanas: Número de semanas
    :return: Una matriz 3D con temperaturas aleatorias
    """
    temperaturas = [[[random.randint(15, 30) for _ in range(num_dias_semana)]
                     for _ in range(num_semanas)]
                    for _ in range(num_ciudades)]
    return temperaturas


# Crear la matriz de temperaturas
temperaturas = generar_temperaturas(num_ciudades, num_dias_semana, num_semanas)

print("Matriz de temperaturas (Ciudades x Días x Semanas):")
for ciudad in range(num_ciudades):
    for semana in range(num_semanas):
        print(f"Ciudad {ciudad + 1}, Semana {semana + 1}: {temperaturas[ciudad][semana]}")


# Calcular el promedio de temperaturas para cada ciudad y semana
def calcular_promedios(temperaturas):
    """
    Calcula el promedio de temperaturas diarias para cada ciudad y cada semana.

    :param temperaturas: Una matriz 3D con temperaturas (Ciudades x Días x Semanas)
    :return: Una matriz 2D con promedios de temperaturas (Ciudades x Semanas)
    """
    # Inicializa una matriz 2D para los promedios
    promedios = [[0] * num_semanas for _ in range(num_ciudades)]

    # Itera sobre cada ciudad
    for ciudad in range(num_ciudades):
        # Itera sobre cada semana
        for semana in range(num_semanas):
            # Extrae las temperaturas para la ciudad y semana actuales
            semana_temperaturas = temperaturas[ciudad][semana]
            # Calcula el promedio de las temperaturas de la semana
            promedio = sum(semana_temperaturas) / len(semana_temperaturas)
            # Guarda el promedio en la matriz de promedios
            promedios[ciudad][semana] = promedio

    return promedios


# Obtener los promedios
promedios = calcular_promedios(temperaturas)

# Mostrar los promedios de temperaturas por ciudad y semana
print("\nPromedio de temperaturas por ciudad y semana:")
for ciudad in range(num_ciudades):
    for semana in range(num_semanas):
        print(f"Ciudad {ciudad + 1}, Semana {semana + 1}: {promedios[ciudad][semana]:.2f} °C")


# Función para calcular el promedio de temperatura de una ciudad durante todas las semanas
def promedio_ciudad(temperaturas, ciudad):
    """
    Calcula el promedio de temperatura para una ciudad durante todas las semanas.

    :param temperaturas: Una matriz 3D con temperaturas (Ciudades x Días x Semanas)
    :param ciudad: Índice de la ciudad para la cual calcular el promedio
    :return: Promedio de temperatura para la ciudad especificada
    """
    # Extrae todas las temperaturas para la ciudad especificada en todas las semanas
    temperaturas_ciudad = [temp for semana in temperaturas[ciudad] for temp in semana]
    # Calcula el promedio de todas las temperaturas
    promedio = sum(temperaturas_ciudad) / len(temperaturas_ciudad)
    return promedio


# Calcular y mostrar el promedio de temperatura para cada ciudad
print("\nPromedio de temperatura total por ciudad:")
for ciudad in range(num_ciudades):
    promedio = promedio_ciudad(temperaturas, ciudad)
    print(f"Ciudad {ciudad + 1}: {promedio:.2f} °C")
