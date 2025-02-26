def desglosar_cantidad(cantidad):
    cantidad = cantidad // 10 * 10
    billetes_y_monedas = [100000, 50000, 20000, 10000, 5000, 2000, 1000, 500, 200, 100, 50]
    desglose = []
    for valor in billetes_y_monedas:
        cantidad_billetes = cantidad // valor  # cantidad de billetes/monedas
        if cantidad_billetes > 0:
            desglose.append(valor)  # añadir al desglose si la cantidad es mayor que cero
        cantidad %= valor  # reducir la cantidad por los billetes/monedas que ya se contaron
    
    return desglose
cantidad = int(input("Ingrese la cantidad de COP: "))
desglose = desglosar_cantidad(cantidad)

print("Desglose: ", ",".join(map(str, desglose)))