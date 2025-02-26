#Entrada
inversion_inicial = float(input("Ingrese el monto de inversión inicial en COP: "))
tasa_interes = float(input("Ingrese la tasa de interés anual en porcentaje: "))
#Caja negra 
monto_minimo_reinversion = 100000
intereses = inversion_inicial * (tasa_interes / 100)

if intereses > monto_minimo_reinversion:
    inversion_final = inversion_inicial + intereses
#Salida    
    print(f"Los intereses generados son: {intereses:.2f} COP")
    print(f"El monto final en la cuenta después de reinvertir los intereses es: {inversion_final:.2f} COP")
else:    
    print(f"Los intereses generados son: {intereses:.2f} COP")
    print(f"El monto en la cuenta se mantiene en: {inversion_inicial:.2f} COP")