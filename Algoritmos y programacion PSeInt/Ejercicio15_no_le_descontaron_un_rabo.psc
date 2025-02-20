Algoritmo Ejercicio15_no_le_descontaron_un_rabo
	// Definición de variables
	Definir precio_final Como Real
	Definir precio_venta_publico Como Real
	Definir porcentaje_descuento Como Real
	
	// Solicitar datos al usuario
	Escribir "Ingrese el precio final pagado por el producto: "
	Leer precio_final
	Escribir "Ingrese el precio de venta al público (PVP) del producto: "
	Leer precio_venta_publico
	
	// Cálculo del porcentaje de descuento
	porcentaje_descuento <- ((precio_venta_publico - precio_final) / precio_venta_publico) * 100
	
	// Mostrar resultado
	Escribir "El porcentaje de descuento aplicado es: ", porcentaje_descuento, "%"
FinAlgoritmo