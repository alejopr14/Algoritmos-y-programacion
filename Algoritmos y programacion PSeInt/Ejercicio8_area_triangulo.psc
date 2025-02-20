Algoritmo Ejercicio8_area_triangulo
  Escribir "Ingrese la medida del lado a"
  Leer a
  Escribir "Ingrese la medida del lado b"
  
  Leer b
  Escribir "Ingrese la medida del lado c"
  Leer c
	
  s=(a+b+c)/2
  area=raiz(s*(s-a)*(s-b)*(s-c))

  Escribir "El Semíperimetro del triangulo es: ", s
  Escribir "El Área del triangulo es: ", area
FinAlgoritmo
