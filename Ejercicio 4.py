#Ejercicio 4

a=0
b=False

def signo(a,b):
    if (a>0):
        return 1
    if (a<0):
        return -1

a=int(input("Por favor, Ingrese un número "))
c=signo(a, b)
    
if (c==1):
    print (a, "es un número positivo")
    
if (c==-1):
    print (a, "es un número negativo")
        