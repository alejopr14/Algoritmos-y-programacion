# Entrada
A = int(input("Ingrese el dígito A (miles): "))
B = int(input("Ingrese el dígito B (centenas): "))
C = int(input("Ingrese el dígito C (decenas): "))
D = int(input("Ingrese el dígito D (unidades): "))
#Caja negra
N = A * 1000 + B * 100 + C * 10 + D
resto = N % 100  
if resto >= 50:
    N_redondeado = (N // 100) * 100 + 100  
else:
    N_redondeado = (N // 100) * 100  

#Salida
print(f"El número redondeado es: {N_redondeado}")