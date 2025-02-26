# Datos de entrada
ventas_departamento1 = float(input("Ingrese las ventas del Departamento 1: "))
ventas_departamento2 = float(input("Ingrese las ventas del Departamento 2: "))
ventas_departamento3 = float(input("Ingrese las ventas del Departamento 3: "))
salario_base = float(input("Ingrese el salario base de los vendedores: "))

#Caja negra
ventas_totales = ventas_departamento1 + ventas_departamento2 + ventas_departamento3
umbral = ventas_totales * 0.33

incentivo_departamento1 = 0
incentivo_departamento2 = 0
incentivo_departamento3 = 0

if ventas_departamento1 > umbral:
    incentivo_departamento1 = salario_base * 0.20
if ventas_departamento2 > umbral:
    incentivo_departamento2 = salario_base * 0.20
if ventas_departamento3 > umbral:
    incentivo_departamento3 = salario_base * 0.20

salario_total_departamento1 = salario_base + incentivo_departamento1
salario_total_departamento2 = salario_base + incentivo_departamento2
salario_total_departamento3 = salario_base + incentivo_departamento3

#Salida
print(f"El salario total de los vendedores del Departamento 1 es: {salario_total_departamento1}")
print(f"El salario total de los vendedores del Departamento 2 es: {salario_total_departamento2}")
print(f"El salario total de los vendedores del Departamento 3 es: {salario_total_departamento3}")