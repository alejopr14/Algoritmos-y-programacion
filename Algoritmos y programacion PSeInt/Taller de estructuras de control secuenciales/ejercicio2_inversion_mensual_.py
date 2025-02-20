def calcular_interes(capital, tasa_interes):
    interes_ganado = capital * tasa_interes
    return interes_ganado

capital_invertido = float(input("Ingresa el capital a invertir: $"))
tasa_interes_mensual = 0.02  

interes = calcular_interes(capital_invertido, tasa_interes_mensual)

print(f"Después de un mes, ganarás: ${interes:.2f}")