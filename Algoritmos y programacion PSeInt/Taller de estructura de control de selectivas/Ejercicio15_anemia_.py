def verificar_anemia(edad, sexo, hemoglobina):
    # Determinar el rango de hemoglobina según la edad y el sexo
    if edad <= 1:
        # 0 meses - 1 mes
        rango_min, rango_max = 13, 26
    elif 1 < edad <= 6:
        # Mayor de 1 mes y menor o igual a 6 meses
        rango_min, rango_max = 10, 18
    elif 6 < edad <= 12:
        # Mayor de 6 meses y menor o igual a 12 meses
        rango_min, rango_max = 11, 15
    elif 1 <= edad <= 5:
        # Mayor de 1 año y menor o igual a 5 años
        rango_min, rango_max = 11.5, 15
    elif 5 < edad <= 10:
        # Mayor de 5 años y menor o igual a 10 años
        rango_min, rango_max = 12.6, 15.5
    elif 10 < edad <= 15:
        # Mayor de 10 años y menor o igual a 15 años
        rango_min, rango_max = 13, 15.5
    elif sexo == 'F' or sexo == 'f':
        # Mujeres mayores de 15 años
        rango_min, rango_max = 12, 16
    else:
        # Hombres mayores de 15 años
        rango_min, rango_max = 14, 18

    # Comparar el nivel de hemoglobina
    if hemoglobina < rango_min:
        return "Anemia: El nivel de hemoglobina es menor al rango mínimo."
    else:
        return "No tiene Anemia: El nivel de hemoglobina está dentro del rango."

# Entrada de datos
edad = int(input("Ingrese la edad de la persona: "))
sexo = input("Ingrese el sexo de la persona (M/F): ").strip()
hemoglobina = float(input("Ingrese el nivel de hemoglobina en g%: "))

# Verificar si tiene anemia
resultado = verificar_anemia(edad, sexo, hemoglobina)

# Mostrar el resultado
print(resultado)