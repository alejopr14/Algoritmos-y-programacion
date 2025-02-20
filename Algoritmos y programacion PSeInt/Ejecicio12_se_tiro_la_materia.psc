Algoritmo  Ejecicio12_se_tiro_la_materia
	// Definición de variables
	Definir nombre_alumno Como Cadena
	Definir nota_examen_matematica Como Real
	Definir nota_tarea1_matematica Como Real
	Definir nota_tarea2_matematica Como Real
	Definir nota_tarea3_matematica Como Real
	Definir promedio_tareas_matematica Como Real
	Definir promedio_matematica Como Real
	
	Definir nota_examen_fisica Como Real
	Definir nota_tarea1_fisica Como Real
	Definir nota_tarea2_fisica Como Real
	Definir promedio_tareas_fisica Como Real
	Definir promedio_fisica Como Real
	
	Definir nota_examen_quimica Como Real
	Definir nota_tarea1_quimica Como Real
	Definir nota_tarea2_quimica Como Real
	Definir nota_tarea3_quimica Como Real
	Definir promedio_tareas_quimica Como Real
	Definir promedio_quimica Como Real
	
	Definir promedio_general Como Real
	
	// Solicitar datos al usuario
	Escribir "Ingrese el nombre del alumno: "
	Leer nombre_alumno
	
	// Datos para Matemática
	Escribir "Ingrese la nota del examen de Matemática: "
	Leer nota_examen_matematica
	Escribir "Ingrese la nota de la tarea 1 de Matemática: "
	Leer nota_tarea1_matematica
	Escribir "Ingrese la nota de la tarea 2 de Matemática: "
	Leer nota_tarea2_matematica
	Escribir "Ingrese la nota de la tarea 3 de Matemática: "
	Leer nota_tarea3_matematica
	
	// Datos para Física
	Escribir "Ingrese la nota del examen de Física: "
	Leer nota_examen_fisica
	Escribir "Ingrese la nota de la tarea 1 de Física: "
	Leer nota_tarea1_fisica
	Escribir "Ingrese la nota de la tarea 2 de Física: "
	Leer nota_tarea2_fisica
	
	// Datos para Química
	Escribir "Ingrese la nota del examen de Química: "
	Leer nota_examen_quimica
	Escribir "Ingrese la nota de la tarea 1 de Química: "
	Leer nota_tarea1_quimica
	Escribir "Ingrese la nota de la tarea 2 de Química: "
	Leer nota_tarea2_quimica
	Escribir "Ingrese la nota de la tarea 3 de Química: "
	Leer nota_tarea3_quimica
	
	// Cálculo del promedio de Matemática
	promedio_tareas_matematica <- (nota_tarea1_matematica + nota_tarea2_matematica + nota_tarea3_matematica) / 3
	promedio_matematica <- (nota_examen_matematica * 0.9) + (promedio_tareas_matematica * 0.1)
	
	// Cálculo del promedio de Física
	promedio_tareas_fisica <- (nota_tarea1_fisica + nota_tarea2_fisica) / 2
	promedio_fisica <- (nota_examen_fisica * 0.8) + (promedio_tareas_fisica * 0.2)
	
	// Cálculo del promedio de Química
	promedio_tareas_quimica <- (nota_tarea1_quimica + nota_tarea2_quimica + nota_tarea3_quimica) / 3
	promedio_quimica <- (nota_examen_quimica * 0.85) + (promedio_tareas_quimica * 0.15)
	
	// Cálculo del promedio general
	promedio_general <- (promedio_matematica + promedio_fisica + promedio_quimica) / 3
	
	// Mostrar resultados
	Escribir "Alumno: ", nombre_alumno
	Escribir "Promedio en Matemática: ", promedio_matematica
	Escribir "Promedio en Física: ", promedio_fisica
	Escribir "Promedio en Química: ", promedio_quimica
	Escribir "Promedio General: ", promedio_general
FinAlgoritmo