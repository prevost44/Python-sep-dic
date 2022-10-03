#Ángel de la Cruz, 21-1380
#Realizar un programa el cual determine el tiempo en meses para pagar un préstamo.
#El monto del préstamo debe ser solicitado.
#Se debe solicitar la cantidad mensual que se desea pagar.
#Mediante el uso de while, determinar los meses (total) en los que se completará el pago del préstamo.

#Bienvenida al programa
print("Bienvenido a PrestamoTimer, su calculadora de préstamos")

#Declaración de variables y solicitud del monto del préstamo y del monto a pagar mensual
prestamo= int(input("Introduzca el monto del préstamo que desea tomar: "))
monto= int(input("Introduzca la cantidad de dinero que desea pagar mensualmente para saldar el préstamo: "))
print("Su préstamo es de ","RD$"+str(prestamo), "y será pagado en cuotas mensuales de ", "RD$"+str(monto)+"." )
x= prestamo 
meses= x/monto
numpago= 0

#While para la impresión del tiempo que durará pagando y cuantos pagos tendrá que hacer
while x > 0:
    print("Luego de su pago #"+str(numpago),"el tiempo que le tomarás saldar su préstamo es: ", meses, "meses.")
    #contador de lo que falta por pagar
    x=x - monto
    #contador del numero de cada pago
    numpago= numpago+1
    #contador de meses segun vayan reduciendose
    meses= meses-1
#condición para indicar con cual pago saldará el préstamo.    
if x <= 0:
    print("Con el pago #"+str(numpago), "su préstamo será totalmente saldado.")
input()