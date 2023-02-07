#Ejercicio 11

a=""
b=""
c=""

def concatenar(a,b):
    
    c= a + " " + b

    return c

a=str(input("Por favor, Ingrese una palabra "))

b=str(input("Por favor, Ingrese otra palabra "))

c=concatenar(a, b)
    
print ("El reultado de concatenar las palabras ingresadas es:",c)
