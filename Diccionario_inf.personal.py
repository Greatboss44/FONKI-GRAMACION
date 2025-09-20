# Diccionario con las claves iniciales
informacion_personal = {
    "nombre": "kaory Cisneros",
    "edad": 30,
    "ciudad": "Joya de los Sachas",
    "profesion": "Ingeniera Civil"
}
#  'ciudad' y modificarlo a una ciudad diferente
print("Ciudad original:", informacion_personal["ciudad"])
informacion_personal["ciudad"] = "Guayaquil"  # cambio de la ciudad

#  Agregar (o actualizar) la clave 'profesion'
informacion_personal["profesion"] = "Profesora universitaria"

# Verificar existencia de la clave 'telefono' y agregarla si no existe
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "099-987-6547se"

# Eliminar la clave 'edad' porque no es necesaria
#   Se usa pop con valor por defecto para evitar error si no existiera.
informacion_personal.pop("edad", None)

#  Se imprimira el diccionario final de forma legible
print("\nDiccionario final:")
print(informacion_personal)















