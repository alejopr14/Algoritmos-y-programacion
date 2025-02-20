#entrada
a = float(input("Ingrese medida lado a: "))
b = float(input("Ingrese medida lado b: "))
c = float(input("Ingrese medida lado c: "))
#caja negra
s = (a + b + c) / 2
area = (s * (s - a) * (s - b) * (s - c))
#salida
print(f"El área del triángulo es: {area:.2f} unidades cuadradas")