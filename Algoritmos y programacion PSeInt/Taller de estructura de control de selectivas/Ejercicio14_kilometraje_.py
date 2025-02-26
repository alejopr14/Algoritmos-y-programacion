def calcular_consumo(lectura_anterior, lectura_actual):
    # Calcular el consumo de Kwh
    return lectura_actual - lectura_anterior

def calcular_monto(consumo):
    # Determinar el costo por Kwh según el rango de consumo
    if consumo <= 100:
        costo_kwh = 4600
    elif 101 <= consumo <= 300:
        costo_kwh = 8000
    elif 301 <= consumo <= 500:
        costo_kwh = 100000
    else:
        costo_kwh = 120000

    # Calcular el monto a pagar
    monto = consumo * costo_kwh
    return monto

# Entrada de datos
lectura_anterior = int(input("Ingrese la lectura anterior del medidor (Kwh): "))
lectura_actual = int(input("Ingrese la lectura actual del medidor (Kwh): "))

# Calcular el consumo
consumo = calcular_consumo(lectura_anterior, lectura_actual)

# Calcular el monto a pagar
monto_a_pagar = calcular_monto(consumo)

# Mostrar el resultado
print(f"El consumo de luz eléctrica es: {consumo} Kwh.")
print(f"El monto a pagar por consumo de luz eléctrica es: {monto_a_pagar} COP.")