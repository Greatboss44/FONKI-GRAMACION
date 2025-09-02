# Promedio de temperaturas por ciudad y semana

# Variables
ciudades = ["Quito", "Guayaquil", "Ambato"]
dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
num_semanas = 2  # 2 semanas


temperaturas = [
    [  # Quito
        [20, 21],  # Lunes (semana 1, semana 2)
        [22, 23],  # Martes
        [19, 20],  # Miércoles
        [21, 22],  # Jueves
        [18, 19],  # Viernes
        [20, 21],  # Sábado
        [21, 22]   # Domingo
    ],
    [  # Guayaquil
        [28, 29],
        [30, 31],
        [29, 28],
        [32, 33],
        [31, 30],
        [30, 29],
        [28, 27]
    ],
    [  # Ambato
        [15, 16],
        [17, 18],
        [16, 17],
        [15, 16],
        [14, 15],
        [15, 16],
        [17, 18]
    ]
]

# Calcular promedio por ciudad y semana
for i, ciudad in enumerate(ciudades):  #  ciudades
    print(f"\nPromedios de temperatura en {ciudad}:")
    for semana in range(num_semanas):
        suma = 0
        for dia in range(len(dias_semana)):  # días
            suma += temperaturas[i][dia][semana]
        promedio = suma / len(dias_semana)
        print(f"  Semana {semana + 1}: {promedio:.2f}°C")
