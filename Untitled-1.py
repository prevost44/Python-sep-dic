#Ángel de la Cruz, 21-1380
#Escribir un programa que capture una lista de caracteres.
#Indicaciones:
#La longitud de la lista debe ser dinámica (capturada).
#Si el usuario ingresa un dígito (cualquiera), se debe terminar la ejecución del programa con el mensaje: "Lo sentimos, no se permiten dígitos.", y mostrar la lista con los caracteres que se lograron capturar (en caso de que se hayan capturado).
#Si el usuario ingresa una palabra, se debe de omitir y continuar con el bucle.
#Mostra la lista con los caracteres capturados y el total.

#Lista donde se almacenarán los valores
lista=[]
#Variable para definir el tamaño de la lista
extra=int(input("Introduce el limite de caracteres: "))

#La condición se ejecutará mientras el largo de la lista (caracteres introducidos) sea distinto al largo decidido por el usuario
while len(lista) != extra:
    #Variable para pedir caracter  
    caracter= (input("Introduce un caracter (NO SE ACEPTAN NÚMEROS): "))
    #Condicion para cuando introduzca un numero, el break es para acabar el programa si se cumple
    if caracter  == "0" or caracter  =="1" or caracter  =="2" or caracter  =="3" or caracter  =="4" or caracter  =="5" or caracter  =="6" or caracter  =="7" or caracter  =="8"or caracter  =="9":
        print("Lo sentimos no se permiten dígitos, la lista que creo fue: ", lista)
        break
    #Condición para cuando se agreguen dos o más caracteres lo ignore y pida otro caracter
    elif len(caracter) >= 2:
        continue  
    #Condición para agregar caracteres a la lista y seguir pidiendo otros     
    else:   
        lista.append(caracter)
        
        
#Impresion cuando la lista llegue al limite asignado por el usuario
print("La lista final fue: ", lista)
input ()