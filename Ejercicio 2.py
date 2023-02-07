#Ejercicio 2

a=0
b=False

def es_positivo(a,b):
    if (a>0):
        return True
    if (a<0):
        return False

a=int(input("Por favor, Ingrese un número "))
c=es_positivo(a, b)
    
if (c==True):
    print (a, "es un número positivo")
    
if (c==False):
    print (a, "es un número negativo")
        