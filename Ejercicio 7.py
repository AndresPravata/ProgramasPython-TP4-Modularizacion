#Ejercicio 7
from math import sqrt
d=float()

def raiz_uno(a, b, c, d):
    
    discriminante = b ** 2 - 4 * a * c

    if discriminante >= 0:
        raiz = sqrt(discriminante)
        d=((-b + raiz) / (2 * a))
        
    return d

a=float(input("Por favor, Ingrese el término a "))
b=float(input("Por favor, Ingrese el término b "))
c=float(input("Por favor, Ingrese el término c "))

d=raiz_uno(a, b, c, d)

print ("La primera raiz de",a,"x^2 +",b,"x + ",c,"= 0 es x =",d)
    