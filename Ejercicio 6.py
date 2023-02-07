#Ejercicio 6

a=0
b=0

def delta_de_dirac(a,b):
    if (a==b):
        return 1
    if (a!=b):
        return 0

a=int(input("Por favor, Ingrese un número "))
b=int(input("Por favor, otro número "))
c=delta_de_dirac(a, b)
    
if (c==1):
    print ("Los numeros ingresados son Iguales")
    
if (c==0):
    print ("Los números ingresados son Distintos")
        