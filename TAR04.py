
#Escriba un programa que permita crear una lista de palabras y que, 
#a continuación, pida una palabra y diga cuántas veces aparece esa palabra en la lista.



#Ponemos algunos input para que se declaren las variables que el usuario quiera.
print("Escriba 5 palabras para crear la lista")
pb1= input("Escriba la primera palabra: ")
pb2= input("Escriba la segunda palabra: ")
pb3= input("Escriba la tercera palabra: ")
pb4= input("Escriba la cuarta palabra: ")
pb5= input("Escriba la quinta palabra: ")

#Juntamos todas las variables en una sola.
variables= [pb1, pb2, pb3, pb4, pb5]

#Hacemos la lista de las palabras que ha escogido el usuario.
print("La lista que has creado es:", variables,)

#Ponemos un input para que el usuario escoga su palabra.
palabra= input("Escriba una palabra: ")
variables.count(palabra)

#Declaramos una variable para que printee cuantas veces se repite la palabra.
x= variables.count(palabra)
if x == 0:
    print("La palabra", palabra, "no esta en la lista.")
else:
    print("La palabra", palabra, "se repite", x, "veces")


input()