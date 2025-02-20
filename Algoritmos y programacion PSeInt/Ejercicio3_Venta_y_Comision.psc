Algoritmo Ejercicio3_SueldoyComisiones
	Definir venta1, venta2, venta3, comision,sueldo Como Real
	Escribir "Escribe las 3 ventas del mes"
	Leer venta1, venta2, venta3
	Escribir "Escribe el sueldo base"
	leer sueldo
	comision = venta1 + venta2 + venta3 * .10
	Escribir "El sueldo base es: $",comision 
	Escribir "La comision del mes es: $", comision
	Escribir "El sueldo total del mes es: $", sueldo + comision
	
	
FinAlgoritmo
