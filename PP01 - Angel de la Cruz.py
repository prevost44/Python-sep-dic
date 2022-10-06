#Angel de la Cruz, 21-1380
#Realice un programa que replique la impresión de una factura, como la que se muestra a continuación:

#Variable para pedir nombre del cliente
from decimal import Rounded


cliente=input("Introduzca su primer nombre y su primer apellido: ")

#listas para guardar productos cantidades precios e itbis
productos=[]
precios=[]
cantidades=[]
itbis=[]
#Listas para poder sumar el total de ITBIS y precio
totalitbis=[]


#Variable para que el usuario diga el maximo de productos a pedir
totalproductos=int(input("Introduzca el total de productos que tendra su factura: "))
#Variables extra para calculos de itbis y condiciones
x=1.18
y=0.18
itt= 250
#While para pedir al usario que introduzca los productos, precios y cantidades del producto, y luego agregarlas a la lista
while len(cantidades) != totalproductos:
    #Variables para solicitar el producto, su precio y la cantidad que desea
    producto=input("Introduzca el nombre del producto que desea ordenar: ")
    precio=float((input("Introduzca el precio de dicho producto (maximo dos decimales): ")))
    cantidad= int(input("Introduzca la cantidad que desea de dicho producto: "))
    #Calculo del precio total, redondeo del mismo y agregación de variables a sus respectivas listas
    real_precio= precio*cantidad
    redprecio=round(real_precio, 2)
    productos.append(producto)
    precios.append(redprecio)
    cantidades.append(cantidad)
    #Condiciones para calcular itbis
    if precio > itt:
        itbis_1= float(((real_precio/x)*y))
        reditbis= round(itbis_1, 2)
        itbis.append("RD$ "+str(reditbis))
        totalitbis.append(itbis_1)
    if precio < itt:   
        itbis.append("RD$ 0.00")
#Impresión de factura
print("╔══════════════════════════════╗")
print("║FACTURA DE CONSUMO ELECTRONICO║")
print("╚══════════════════════════════╝")
print("╔══════════════════════════════╗")
print("║Consumidor:",cliente, "\t""\b""║")
print("╚══════════════════════════════╝", "\n")
print("╔════════════════╦═══════════════╦═══════════════╦══════════════╗")
print("║Cantidad","\t","║Producto","\t","║ITBIS\t\t","║Precio\t"+"║")
print("╚════════════════╩═══════════════╩═══════════════╩══════════════╝")
#Contador para imprimir los productos en orden con sus precios, cantidades e itbis correspondiente
w=0
while w != totalproductos:
    print("║",str(cantidades[w]),"\t","\t", "║"+str(productos[w]+" "),"\t","║"+str((itbis[w]))+"\t","║"+"RD$ "+str(precios[w]),"\t"+"║")
    print("╚════════════════╩═══════════════╩═══════════════╩══════════════╝")
    w=w+1
#Suma del total de precios e itbis, e impresión de la misma
suma_itbis= sum(totalitbis)
suma_precios= sum(precios)
red_sumaitbis=round(suma_itbis, 2)

red_sumaprecios=round(suma_precios, 2)
print("╔════════════════════════════════╦═══════════════╦══════════════╗")
print("║","\t""   TOTAL A PAGAR:   ","\t","║", "RD$"+str(red_sumaitbis)+"\t","║", "RD$ "+str(red_sumaprecios),"\t"+"║")
print("╚════════════════════════════════╩═══════════════╩══════════════╝")



input()