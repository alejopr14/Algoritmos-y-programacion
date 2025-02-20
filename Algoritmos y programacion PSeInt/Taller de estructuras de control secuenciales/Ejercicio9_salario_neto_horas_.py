#entrada
horas_trabajadas = float(input("Ingrese el número de horas trabajadas: "))
precio_por_hora = float(input("Ingrese el precio por hora: "))
#caja negra
sueldo_base = (horas_trabajadas * precio_por_hora)
descuento_impuestos = (sueldo_base * 0.20)
salario_neto = sueldo_base - descuento_impuestos
#salida
print(f"Sueldo base: {sueldo_base:.2f} $")
print(f"Descuento por impuestos: {descuento_impuestos:.2f} $")
print(f"Salario neto: {salario_neto:.2f} $")