# Promedio de temperaturas por ciudad y semana

# Variables
ciudades = ["Quito", "Guayaquil", "Ambato"]
dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
num_semanas = 4  # 4 semanas


temperaturas = [
    [  # Quito
        [20, 21, 17, 20],  # Lunes (semana 1, semana 2, semana 3, semana 4)
        [22, 23, 16, 18],  # Martes
        [19, 20, 22, 19],  # Miércoles
        [21, 22, 19, 23],  # Jueves
        [18, 19, 20, 17],  # Viernes
        [20, 21, 20, 19],  # Sábado
        [21, 22, 22, 19]   # Domingo
    ],
    [  # Guayaquil
        [28, 29, 25, 28],
        [30, 31,32 , 26],
        [29, 28, 33, 30],
        [32, 33, 28, 34],
        [31, 30, 34, 30],
        [30, 29, 34, 29],
        [28, 27, 30, 27 ]
    ],
    [  # Ambato
        [15, 16, 13, 14],
        [14, 15, 16, 15],
        [17, 18, 19, 18]    ,
        [16, 17, 18, 16],
        [15, 16, 18, 15],
        [14, 15, 19, 15],
        [17, 18, 19, 18],

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
