#entrada
parcial_1 = float(input("Calificacion primer parcial: "))
parcial_2 = float(input("Calificacion segundo parcial: "))
parcial_3 = float(input("Calificacion tercer parcial: "))
calificacion_examen_final = float(input("Ingresa la calificación del examen final: "))
calificacion_trabajo_final = float(input("Ingresa la calificación del trabajo final: "))

# caja negra
promedio_parciales = (parcial_1 + parcial_2 + parcial_3) / 3
calificacion_final = (promedio_parciales * 0.55) + (calificacion_examen_final * 0.30) + (calificacion_trabajo_final * 0.15)

#salida
print(f"La calificación final en la materia de computación es: {calificacion_final:.2f}")