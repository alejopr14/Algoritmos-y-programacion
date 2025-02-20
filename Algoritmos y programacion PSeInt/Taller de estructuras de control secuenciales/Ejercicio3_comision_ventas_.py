sueldo_base = float(input("ingrese su sueldo base"))

venta1 = float(input("ingrese valor primer venta"))
venta2 = float(input("ingrese valor segunda venta"))
venta3 = float(input("ingrese valor tercer venta"))

total_ventas = venta1 + venta2 + venta3
comisiones = total_ventas * 0.10
total_a_recibir = sueldo_base + comisiones

print(f"Total de comisiones: ${comisiones:.2f}")
print(f"Total a recibir (sueldo base + comisiones): ${total_a_recibir:.2f}")