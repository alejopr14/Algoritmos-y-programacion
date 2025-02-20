Algoritmo Ejercicio9_salario_neto_trabajador
    Escribir "Ingrese su salario Base Mensual"
	Leer Smensual
	Escribir "Ingrese la cantidad de horas trabajadas al mes"
	Leer Horas
	
	SalarioBasepordia= (Smensual/30)
	SalarioBaseporhora= (SalarioBasepordia/8)
	SalarioNetopordia= (SalarioBasepordia*0.8)
	SalarioNetoporhora= (SalarioNetopordia/8)
	SalarioNETO= (SalarioNetoporhora*Horas)
	SalarioNETO1=trunc(SalarioNETO)
	
	Escribir "Salario NETO: ", SalarioNETO1 , " por ", Horas " trabajadas al mes"
FinAlgoritmo
