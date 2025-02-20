Algoritmo Ejercicio21_Mi_pc_gamer
	// Definición de variables
	Definir P Como Real
	Definir T Como Real
	Definir monto_total_cuotas Como Real
	Definir porcentaje_recargo Como Real
	
	// Solicitar datos al usuario
	Escribir "Ingrese el precio al contado (P) del computador: "
	Leer P
	Escribir "Ingrese el monto de cada cuota (T) en COP: "
	Leer T
	
	// Cálculo del monto total en cuotas
	monto_total_cuotas <- T * 12
	
	// Cálculo del porcentaje de recargo
	porcentaje_recargo <- ((monto_total_cuotas - P) / P) * 100
	
	// Mostrar resultado
	Escribir "El porcentaje de recargo en el pago por cuotas es: ", porcentaje_recargo, "%"
FinAlgoritmo