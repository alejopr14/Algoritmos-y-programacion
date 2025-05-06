estudiantes = {}

for i in range(1, 11):
    print(f"Estudiante_numero {i}:")
    nombre = input("Nombre: ")
    nota = float(input("Nota: "))
    estudiantes[str(i)] = {"nombre": nombre, "nota": nota}

aprobados = []
suspensos = []
suma_notas = 0

for datos in estudiantes.values():
    nota = datos["nota"]
    suma_notas += nota
    if nota >= 5:
        aprobados.append(datos["nombre"])
    else:
        suspensos.append(datos["nombre"])

media = suma_notas / len(estudiantes)

print("Estudiantes aprobados:", aprobados)
print("Estudiantes suspendidos:", suspensos)
print(f"Nota media de la clase: {media:.2f}")
