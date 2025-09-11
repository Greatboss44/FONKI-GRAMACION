# Calculo de descuentos
# El  programa define una función para calcular descuentos
# y luego realiza llamadas a la función con distintos parámetros.

# Definición de la función

def calcular_descuento(monto_total, porcentaje_descuento=10):

    descuento = (monto_total * porcentaje_descuento) / 100
    return descuento



def main():
   #descuento del 10%
    monto1 = 200.0
    descuento1 = calcular_descuento(monto1)
    total1 = monto1 - descuento1

    print("Compra 1:")
    print(f"Monto total: ${monto1:.2f}")
    print(f"Descuento aplicado: ${descuento1:.2f}")
    print(f"Monto final a pagar: ${total1:.2f}\n")


    monto2 = 350.0
    porcentaje = 15
    descuento2 = calcular_descuento(monto2, porcentaje)
    total2 = monto2 - descuento2
# descuento del 15%
    print("Compra 2:")
    print(f"Monto total: ${monto2:.2f}")
    print(f"Descuento aplicado ({porcentaje}%): ${descuento2:.2f}")
    print(f"Monto final a pagar: ${total2:.2f}")
if __name__ == "__main__":
    main()

