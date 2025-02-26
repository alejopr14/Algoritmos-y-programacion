def calcular_aumento(categoria, salario_bruto):
    if categoria == 1:
        aumento = 0.10  
        salario_base = 5000000
    elif categoria == 2:
        aumento = 0.15 
        salario_base = 4300000
    elif categoria == 3:
        aumento = 0.20 
        salario_base = 3600000
    elif categoria == 4:
        aumento = 0.40 
        salario_base = 2000000
    elif categoria == 5:
        aumento = 0.60 
        salario_base = 900000
    else:
        return "Categoría inválida"
    
    # Calcular el aumento en base al salario bruto
    aumento_salario = salario_base * aumento
    nuevo_salario = salario_base + aumento_salario
    
    return aumento_salario, nuevo_salario

# Entrada de datos
categoria = int(input("Ingrese la categoría del trabajador (1-5): "))
salario_bruto = float(input("Ingrese el salario bruto del trabajador en COP: "))

# Calcular aumento y salario actualizado
resultado = calcular_aumento(categoria, salario_bruto)

# Mostrar los resultados
if isinstance(resultado, tuple):
    aumento_salario, nuevo_salario = resultado
    print(f"Categoría: {categoria}")
    print(f"Salario bruto: {salario_bruto:.2f} COP")
    print(f"Aumento: {aumento_salario:.2f} COP")
    print(f"Nuevo salario: {nuevo_salario:.2f} COP")
else:
    print(resultado)