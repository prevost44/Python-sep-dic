print("Ángel de la Cruz, 21-1380")
#Mensaje de bienvenida
print ("Bienvenido a tu calculadora de operaciones aritméticas")

#os nos habilita las funcionalidades del sistema operativo para poder agregar "cls" comando para limpiar consola
import os
#time nos permite manejar un intervalo 
import time

#Declarar las variables como int (entero), porque por defecto las asumía como string y no permitía realizar las operaciones
#Líneas para solicitar al usuario los números
primernumero = int (input ("Introduzca su primer número:"))
segundonumero = int (input ("Introduzca su segundo número:"))

#Fórmulas e impresión de las operaciones aritméticas
suma= primernumero+segundonumero
print ("El resultado de la suma de ", primernumero, "+", segundonumero, "es", suma   )
resta= primernumero-segundonumero
print ("El resultado de la resta de ", primernumero, "-", segundonumero, "es", resta   )
multiplicacion= primernumero*segundonumero
print ("El resultado de la multiplicación de ", primernumero, "*", segundonumero, "es", multiplicacion  )
division= primernumero/segundonumero
print ("El resultado de la división de ", primernumero, "+", segundonumero, "es", division   )

#Las siguientes líneas indican que luego de cinco segundos se limpiará la consola
print("La consola se limpiará en 5 segundos, en caso de querer conservar los resultados favor de tomar captura.")
time.sleep(5)
os.system("cls")
#Debajo de este comentario no hay más líneas de código