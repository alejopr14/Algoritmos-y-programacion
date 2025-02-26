# Entrada
P = int(input("Ingrese el valor de P: "))
Q = int(input("Ingrese el valor de Q: "))
#Caja negra 
resultado = P**3 + Q**4 - 2*P**2
#Salida
if resultado > 680:
    print("P y Q satisfacen la expresión: P = " + str(P) + ", Q = " + str(Q))
else:
    print("P y Q no satisfacen la expresión: P = " + str(P) + ", Q = " + str(Q))