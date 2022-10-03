#Ángel de la Cruz, 21-1380
#Escriba un programa que pregunte al usuario los números de su ticket de lotería 
#los almacene en una lista y los muestre por pantalla ordenados de menor a mayor.

#Bienvenida del programa
print("Bienvenid@ a tu verificadora de tickets Loto Pool.")
print("A continuación le estaremos solicitando los números de su boleto, para luego proceder a organizarlos de manera ascendente.")

#Solicitud de los números jugados
num1 =input("Por favor inserte su primer número: ")
num2=input("Por favor inserte su segundo número: ")
num3=input("Por favor inserte su tercer número: ")
num4=input("Por favor inserte su cuarto número: ")
num5=input("Por favor inserte su quinto número: ")

#Lista
Boleto = [num1, num2, num3, num4, num5]
#Función para ordenar la lista
Boleto.sort ()
print("Los números correspondientes a su ticket son:", str(Boleto))
print("¡Ha sido todo un placer servirle, suerte con el sorteo!")
input()