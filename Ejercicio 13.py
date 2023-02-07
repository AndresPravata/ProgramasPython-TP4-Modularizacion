#Ejercicio 13

b=int()

def buscar_letra (b):
    a=len(frase)
    frase==frase.lower()
    letra==letra.lower()
    i=0

    for i in range (0,a):
           
        if (frase[i]==letra):
            b=b+1    
    
    return b

frase=str(input("Por favor, Ingrese una frase "))
letra=str(input("Por favor, Ingrese una letra "))

b=buscar_letra(b)
   
print ("En la frase ingresada hay",b,"letras",letra)
