#Ejercicio 14

def capitalizar (b):
    
    global d,c,palabra,i
    
    palabra=palabra.lower()
        
    c=palabra.upper()[0]

    for i in range (1,len(palabra)):
        c=c+(palabra [i])     
    
    return b

b=int ()

palabra=str(input("Por favor, Ingrese una palabra "))
         
capitalizar(b)  
          
print (c)




    