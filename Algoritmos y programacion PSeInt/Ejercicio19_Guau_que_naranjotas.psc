Algoritmo Ejercicio19_Guau_que_naranjotas
	// Definición de variables
	Definir X Como Entero
	Definir U Como Real
	Definir K Como Real
	Definir costo_total Como Real
	Definir ganancia Como Real
	Definir porcentaje_ganancia Como Real
	
	// Solicitar datos al usuario
	Escribir "Ingrese el número de naranjas (X): "
	Leer X
	Escribir "Ingrese el costo por docena (U) en Bolívares: "
	Leer U
	Escribir "Ingrese el ingreso total obtenido (K) en Bolívares: "
	Leer K
	
	// Cálculo del costo total
	costo_total <- (X / 12) * U
	
	// Cálculo de la ganancia
	ganancia <- K - costo_total
	
	// Cálculo del porcentaje de ganancia
	porcentaje_ganancia <- (ganancia / costo_total) * 100
	
	// Mostrar resultado
	Escribir "El porcentaje de ganancia obtenida es: ", porcentaje_ganancia, "%"
FinAlgoritmo