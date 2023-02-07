#Ejercicio 12

a=""
b=""
c=""

def concatenar(a,b):
    
    c= a + b

    return c


a=str(input("Por favor, Ingrese una palabra "))

b=str(input("Por favor, Ingrese otra palabra "))

c=concatenar(a, b)
    
print ("El reultado de concatenar las palabras ingresadas es:",c)


def concatenar2(a,b):
    i=0   
    
    for i in len(a)+len(b):
              
        if i!= " ":
            c= a + " " + b           
    return b
    
    c= a + " " + b

    return c




