def calcular_descuento(monto):
    if monto < 50000:
        descuento = 0
    elif 50000 <= monto <= 100000:
        descuento = 0.05 
    elif 100000 < monto <= 700000:
        descuento = 0.11 
    elif 700000 < monto <= 1500000:
        descuento = 0.18  
    else:
        descuento = 0.25  
    
    monto_descuento = monto * descuento
    monto_total = monto - monto_descuento
    
    return descuento, monto_total, monto_descuento

nombre_cliente = input("Ingrese el nombre del cliente: ")
monto_compra = float(input("Ingrese el monto de la compra en COP: "))

descuento, monto_total, monto_descuento = calcular_descuento(monto_compra)

#Salida
if descuento == 0:
    print(f"{nombre_cliente}, el monto de la compra es: {monto_compra:.2f} COP")
    print("No hay descuento aplicado.")
    print(f"El monto a pagar es: {monto_compra:.2f} COP")
else:
    print(f"{nombre_cliente}, el monto de la compra es: {monto_compra:.2f} COP")
    print(f"Descuento recibido: {monto_descuento:.2f} COP")
    print(f"El monto a pagar después del descuento es: {monto_total:.2f} COP")