Algoritmo Ejercicio5_Calificacion_Final
	Definir a,b,c,examen_final,promedio,calificacion_final Como Real
	Escribir "Escriba la nota de las tres calificaciones"
	Leer a,b,c
	Escribir "Escriba la nota de su examen_final"
	Leer examen_final
	Escribir "Escriba la nota de su trabajo_final"
	Leer trabajo_final 
	promedio = (a+b+c)/3
	calificacion_final=(promedio * .55)+(examen_final*.30)+(trabajo_final*.15)
	Escribir "Su calificacion final es ",calificacion_final
	
	
FinAlgoritmo
	