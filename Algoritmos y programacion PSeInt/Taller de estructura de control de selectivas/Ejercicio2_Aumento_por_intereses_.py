#Entrada
sueldo = float(input("Ingrese el sueldo del trabajador en COP: "))
#Caja negra 
if sueldo < 900000:
    aumento = 0.15  # Aumento del 15%
else:
    aumento = 0.12  # Aumento del 12%
nuevo_sueldo = sueldo + (sueldo * aumento)
#Salida
print(f"El nuevo sueldo del trabajador es: {nuevo_sueldo:.2f} COP")