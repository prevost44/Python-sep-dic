

caracteres=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z"]
numeros=["0","1","2","3","4","5","6","7","8","9"]
lista=[]*10
caracter= (input("Introduce un caracter (NO SE ACEPTAN NÚMEROS): ")).lower
while True:  
    if caracter in caracteres:
     caracter=input("Agregue otro caracter")
     lista.append(caracter)
    if caracter not in caracteres:
        continue 
    caracter=input("Agregue otro caracter")
    if caracter is int:
        break
    print("Lo sentimos no se permiten dígitos, la lista que creo fue: ", lista)
    
while lista  == 10:
    print("La lista final fue: ", lista)


input ()
