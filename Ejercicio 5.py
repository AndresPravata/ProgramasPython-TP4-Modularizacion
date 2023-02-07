#Ejercicio 5

a=0
b=False

def escalon(a,b):
    if (a>0):
        return 1
    if (a<0):
        return 0

a=int(input("Por favor, Ingrese un número "))
c=escalon(a, b)
    
if (c==1):
    print (a, "es un número positivo")
    
if (c==0):
    print (a, "es un número negativo")
        