numero = int(input("Ingrese un número: "))

suma = 0

for i in range(1, numero):
    if numero % i == 0:
        suma = suma + i
        
if suma == numero:
    print("Es un número perfecto.")
else:
    print("No es un número perfecto.")