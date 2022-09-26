from numbers import Number

#programa que imprima la tabla de multiplicar de un numero introducido por teclado
num= int(input("Introduzca el numero del cual desee su tabla de multiplicar hasta el 10: "))
x=1
while x <= 10 :   
    print (str(num), "x", str(x), "=", num*x)
    x= x + 1      
input ()    