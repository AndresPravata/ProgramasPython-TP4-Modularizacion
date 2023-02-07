#Ejercicio 8

a=0
b=0


def pertenece(a,b):
    
    if (n>a) and (n<b):
        print ("El Número Ingresado pertenece al intervalo [",a,";",b,"]")
        
        return True
    else:
        print ("El Número Ingresado no pertenece al intervalo [",a,";",b,"]")

        return False
    
a=int(input("Por favor, Ingrese el límite inferior del intervalo "))
b=int(input("Por favor, Ingrese el límite superior del intervalo "))
   
while (b<a):
        
    b=int(input("Por favor, Ingrese el límite superior del intervalo ")) 
          

n=int(input("Por favor, Ingrese un número "))

c=pertenece(a, b)
    
