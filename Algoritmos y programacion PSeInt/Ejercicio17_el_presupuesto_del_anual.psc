Algoritmo Ejercicio17_el_presupuesto_del_anual
	// Definición de variables
	Definir presupuesto_total Como Real
	Definir presupuesto_ginecologia Como Real
	Definir presupuesto_pediatria Como Real
	Definir presupuesto_traumatologia Como Real
	
	// Solicitar datos al usuario
	Escribir "Ingrese el presupuesto total anual del hospital: "
	Leer presupuesto_total
	
	// Cálculo del presupuesto para cada área
	presupuesto_ginecologia <- presupuesto_total * 0.40
	presupuesto_pediatria <- presupuesto_total * 0.30
	presupuesto_traumatologia <- presupuesto_total * 0.30
	
	// Mostrar resultados
	Escribir "Presupuesto para Ginecología: ", presupuesto_ginecologia, " COP"
	Escribir "Presupuesto para Pediatría: ", presupuesto_pediatria, " COP"
	Escribir "Presupuesto para Traumatología: ", presupuesto_traumatologia, " COP"
FinAlgoritmo