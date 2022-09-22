#Ángel de la Cruz, 21-1380
#Escriba un programa que calcule el precio a pagar por el suministro de energía eléctrica. 
#Se debe preguntar la cantidad de kwh consumidos y el tipo de instalación: R para residencias, I para industrias y C para comercios. 
#Calcule el precio a pagar de acuerdo con la siguiente tabla (está en la plataforma):

#Valores de las variables que indican el tipo de instalaci
R= "residencial"
C= "comercial"
I= "industrial"

#Presentación del programa
print ("Calculadora de tarifa suministro eléctrico.")

#tipolocal guarda el valor introducido para saber si es residencial, comercial o industrial
tipolocal = input("Si el local es un residencial introduzca una R, si es comercial introduzca una C y si es industrial una I:")

#Proceso cuando la instalación sea residencial
if tipolocal == "R":
    print("Hemos detectado que el tipo de instalación de su local corresponde a", str(R)+".")
    consumo1 = int(input("Proceda a introducir su consumo mensual, en kWh:"))
    if consumo1 <= 500:
        print ("Debido a que su consumo es igual o inferior a 500 kWh, el monto a pagar es RD$550.00.")
    elif consumo1 > 500:
        print ("Debido a que su consumo es superior a 500 kWh, el monto a pagar es RD$850.00.")

#Proceso cuando la instalación sea comercial        
if tipolocal == "C":
    print("Hemos detectado que el tipo de instalación de su local corresponde a", str(C)+".")
    consumo2 = int(input("Proceda a introducir su consumo mensual, en kWh:"))
    if consumo2 <= 1000:
        print ("Debido a que su consumo es igual o inferior a 1000 kWh, el monto a pagar es RD$1,300.00.")
    elif consumo2 > 1000:
        print ("Debido a que su consumo es superior a 1000 kWh, el monto a pagar es RD$2,500.00.")

#Proceso cuando la instalación sea industrial
if tipolocal == "I":
    print("Hemos detectado que el tipo de instalación de su local corresponde a", str(I)+".")
    consumo3 = int(input("Proceda a introducir su consumo mensual, en kWh:"))
    if consumo3 <= 5000:
        print ("Debido a que su consumo es igual o inferior a 5000 kWh, el monto a pagar es RD$3,800.00.")
    elif consumo3 > 5000:
        print ("Debido a que su consumo es superior a 5000 kWh, el monto a pagar es RD$4,200.00.")
#Este es el final