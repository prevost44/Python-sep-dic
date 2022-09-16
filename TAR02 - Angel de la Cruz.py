#Angel de la Cruz, 21-1380
import math
#Escribir un programa que pida 2 números y muestre paso a paso el cálculo de la raíz cuadrada de la suma del cuadrado de ambos. Ver fórmula:
#Presentacion del ejercicio
print("Calculadora de raíz cuadrada y potencias")
print("El resultado que arrojara la calculadora es el de la siguiente operacion: √((a^2+b^2 ) )")
#Lineas solicitando los numeros
a= int(input("Introduzca el primer numero (a): "))
b= int(input("Introduzca el segundo numero (b): "))
#Formulas de las potencias
a2= a**2
b2= b**2
print("El resultado de", str(a,)+str("²"), "es: ", a2)
print("El resultado de", str(b,)+str("²"), " es: ", b2)
#Suma de los cuadrados
c= a2 + b2
print("El resultado de la suma de los cuadrados es igual a: ", c)
#Raiz cuadrada de la suma de los cuadrados
raiz= math.sqrt (c)
print("La raiz cuadrada de √(a²+b²) da como resultado: ", raiz)
input()