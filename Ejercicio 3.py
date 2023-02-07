#Ejercicio 3

a=""
b=""
c=False

def iguales(a,b):
    if (a==b):
        return True
    if (a!=0):
        return False

a=str(input("Por favor, Ingrese una palabra "))
b=str(input("Por favor, Ingrese otra palabra "))
c=iguales(a, b)
    
if (c==True):
    print ("Las palabras ingresadas son iguales")
    
if (c==False):
    print ("Las palabras ingresadas son distintas")
        