lista = [12, 23, 5, 12, 92, 5, 12, 5, 29, 92, 64, 23]
contador = {}

for numero in lista:
    if numero in contador:
        contador[numero] += 1
    else:
        contador[numero] = 1

print(contador)