#Ejercicio 9

b=int()
c=0
d=0
i=0

def vocales(a,b):
    for i in a:
              
        if i in "aeiouAEIOU":
            b=b+1
           
    return b

a=str(input("Por favor, Ingrese una palabra "))

b=vocales(a, b)

print ("En la palabra ingresada hay ",b,"vocales")
