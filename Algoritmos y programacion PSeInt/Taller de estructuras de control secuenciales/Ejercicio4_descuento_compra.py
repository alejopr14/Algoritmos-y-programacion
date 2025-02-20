#entrada
total_compra = float(input("Ingresa el total de la compra: "))

# caja negra
descuento = total_compra * 0.15
total_pagar = total_compra - descuento
#salida
print(f"El total a pagar después del descuento es: {total_pagar:.2f}")
	
