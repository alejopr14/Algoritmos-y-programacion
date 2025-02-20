Algoritmo Ejercicio11_la_vida_del_trabajador
	// Definición de variables
	Definir nombre Como Cadena
	Definir horas_normales Como Entero
	Definir pago_hora_normal Como Real
	Definir horas_extras Como Entero
	Definir num_hijos Como Entero
	Definir sueldo_base Como Real
	Definir pago_hora_extra Como Real
	Definir pago_horas_extras Como Real
	Definir sueldo_bruto Como Real
	Definir deduccion_pago_forzoso Como Real
	Definir deduccion_politica_habitacional Como Real
	Definir deduccion_caja_ahorro Como Real
	Definir total_deducciones Como Real
	Definir asignacion_actualizacion_academica Como Real
	Definir asignacion_por_hijo Como Real
	Definir prima_por_hogar Como Real
	Definir total_asignaciones Como Real
	Definir sueldo_neto Como Real
	
	// Solicitar datos al usuario
	Escribir "Ingrese el nombre del trabajador: "
	Leer nombre
	Escribir "Ingrese el número de horas normales trabajadas: "
	Leer horas_normales
	Escribir "Ingrese el pago por hora normal: "
	Leer pago_hora_normal
	Escribir "Ingrese el número de horas extras trabajadas: "
	Leer horas_extras
	Escribir "Ingrese el número de hijos: "
	Leer num_hijos
	
	// Cálculo del sueldo base
	sueldo_base <- horas_normales * pago_hora_normal
	
	// Cálculo del pago por horas extras
	pago_hora_extra <- pago_hora_normal * 1.25
	pago_horas_extras <- horas_extras * pago_hora_extra
	
	// Cálculo del sueldo bruto
	sueldo_bruto <- sueldo_base + pago_horas_extras
	
	// Cálculo de las deducciones
	deduccion_pago_forzoso <- sueldo_base * 0.05
	deduccion_politica_habitacional <- sueldo_base * 0.02
	deduccion_caja_ahorro <- sueldo_base * 0.07
	total_deducciones <- deduccion_pago_forzoso + deduccion_politica_habitacional + deduccion_caja_ahorro
	
	// Cálculo de las asignaciones
	asignacion_actualizacion_academica <- 250000
	asignacion_por_hijo <- 173000 * num_hijos
	prima_por_hogar <- 180000
	total_asignaciones <- asignacion_actualizacion_academica + asignacion_por_hijo + prima_por_hogar
	
	// Cálculo del sueldo neto
	sueldo_neto <- sueldo_bruto + total_asignaciones - total_deducciones
	
	// Mostrar resultados
	Escribir "Trabajador: ", nombre
	Escribir "Sueldo Base: ", sueldo_base, " COP"
	Escribir "Pago por Horas Extras: ", pago_horas_extras, " COP"
	Escribir "Sueldo Bruto: ", sueldo_bruto, " COP"
	Escribir "Total Deducciones: ", total_deducciones, " COP"
	Escribir "Total Asignaciones: ", total_asignaciones, " COP"
	Escribir "Sueldo Neto: ", sueldo_neto, " COP"
FinAlgoritmo
