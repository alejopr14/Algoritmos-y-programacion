Algoritmo Ejercicio13_cantidad_exacta_billetes
	// Definición de variables
	Definir N1 Como Entero
	Definir N2 Como Entero
	Definir N3 Como Entero
	Definir N4 Como Entero
	Definir N5 Como Entero
	Definir N6 Como Entero
	Definir N7 Como Entero
	Definir N8 Como Entero
	Definir total_dinero Como Real
	
	// Solicitar datos al usuario
	Escribir "Ingrese el número de billetes de 50000: "
	Leer N1
	Escribir "Ingrese el número de billetes de 20000: "
	Leer N2
	Escribir "Ingrese el número de billetes de 10000: "
	Leer N3
	Escribir "Ingrese el número de billetes de 5000: "
	Leer N4
	Escribir "Ingrese el número de billetes de 2000: "
	Leer N5
	Escribir "Ingrese el número de billetes de 1000: "
	Leer N6
	Escribir "Ingrese el número de billetes de 500: "
	Leer N7
	Escribir "Ingrese el número de billetes de 100: "
	Leer N8
	
	// Cálculo del total de dinero
	total_dinero <- (N1 * 50000) + (N2 * 20000) + (N3 * 10000) + (N4 * 5000) + (N5 * 2000) + (N6 * 1000) + (N7 * 500) + (N8 * 100)
	
	// Mostrar resultado
	Escribir "El total de dinero en el banco es: ", total_dinero, " COP"
FinAlgoritmo