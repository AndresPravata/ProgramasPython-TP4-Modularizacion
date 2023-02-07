#Ejercicio 1
import math
a=0
b=0

def potencia2(a,b):
    b=a**2
    return b

for i in range (0,5):   
    a=int(input("Por favor, Ingrese un número "))
    b=potencia2(a, b)
    print (a,"^ 2 =",b)    