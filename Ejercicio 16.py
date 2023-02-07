#Ejercicio 16
import math
a=0
b=0
c=0

def pares(a,b):
    d=0

    for a in range (a,b):
        c=a%2
        if (c==0):
            d=d+1 
       
    return d
          
a=int(input("Por favor, Ingrese el límite inferior del intervalo "))
b=int(input("Por favor, Ingrese el límite superior del intervalo "))
   
while (b<=a):
        
    b=int(input("Por favor, Ingrese el límite superior del intervalo "))        

    
d=pares(a, b)

print ("La cantidad de números pares en el intervalo [",a,";",b,"] son:",d)
