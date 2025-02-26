def resolver_ecuacion_segundo_grado(A, B, C):
    # Calcular el discriminante
    D = B**2 - 4 * A * C
    
    if D > 0:
        # Dos soluciones reales
        X1 = (-B + math.sqrt(D)) / (2 * A)
        X2 = (-B - math.sqrt(D)) / (2 * A)
        return f"Las soluciones son X1 = {X1} y X2 = {X2}"
    
    elif D == 0:
        # Una única solución real
        X = -B / (2 * A)
        return f"La única solución es X1 = X2 = {X}"
    
    else:
        # No tiene soluciones reales
        return "La ecuación no tiene solución en los números reales."

# Entrada de datos
A = float(input("Ingrese el valor de A: "))
B = float(input("Ingrese el valor de B: "))
C = float(input("Ingrese el valor de C: "))

# Resolver la ecuación
resultado = resolver_ecuacion_segundo_grado(A, B, C)

# Mostrar el resultado
print(resultado)