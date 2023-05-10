#Determinar si un numeros es par o inpar

def parImpar(num):
#Le decimos que si se divide entre 2 y no da residuos es par'
    if num%2==0:
        #print('par')
        return 'par'
#Le decimos que si se divide entre 2 y da residuos es impar
    else:
        #print('impar')
        return 'impar'
#Mostramos el resultado determinando el numero que ponga en la funcion

print(parImpar(36))
parImpar(5)
parImpar(2)
parImpar(7)
#Codigo para saber si un numero es perfecto
def perfecto(num):
    #Creamos una variable suma que tiene un valor de 0
    sum=0
    #Creamos un ciclo for para saber si se puede dividir entre si
    for i in range(1,num):
        if num%i==0:
            sum+=i
    if sum==num:
        #Si es verdadero mostrara perfecto de lo contrario no es perfecto
        #"print('perfecto')
        return 'perfecto'
    else:
       # print('no esperfecto')
        return 'no es perfecto'

perfecto(6)   
perfecto(10)   
print(perfecto(28))
perfecto(21)   