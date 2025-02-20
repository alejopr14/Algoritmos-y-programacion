#entrada
metros = float(input("Introduce la cantidad en metros: "))
#caja negra
pulgadas_totales = metros * 39.27
pies =int(pulgadas_totales // 12)
pulgadas = pulgadas_totales % 12
#salida
print(f"{metros} metros son {pies} pies y {pulgadas:.2f} pulgadas.")
