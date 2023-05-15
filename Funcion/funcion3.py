
import random
def llenarLista(tam,rango):
    #Creamos una lista con numeros aleatorios
    lista=[random.randrange(rango) for i in range(tam)]    
    return lista

def sumaLista(lista):
    #creamos una variable suma
    sum=0
    #Hacemos un ciclo for
    for x in lista:
        sum+=x
    return sum

#Sacamos el promedio de la lista

def promedioLista(lista):
    return sumaLista(lista)/len(lista)


l1=llenarLista(3,10)
print(l1)



def mayorlis(lista):
    for i in range(len(lista)-1):
        for j in range(i+1, len(l1)):
            if lista[i]>lista[j]:
                lista[i],lista[j]=lista[j],lista[i]
            return lista

def mayornum(lista):
    mayor=lista[0]
    for num in lista:
        if num>mayor:
            mayor=num
    return mayor

def menornum(lista):
    menor=lista[0]
    for num in lista:
        if num<menor:
            menor=num
    return menor

def ascendenteLista(lista):
   
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            if lista[i] > lista[j]:
                lista[i], lista[j] = lista[j], lista[i]
    return lista



def decendente(lista):
   
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            if lista[i] < lista[j]:
                lista[i], lista[j] = lista[j], lista[i]
    return lista


def moda(lista):
    frecuencias = {}
    max_frecuencia = 0
    moda = None
    for elemento in lista:
        if elemento not in frecuencias:
            frecuencias[elemento] = 1
        else:
            frecuencias[elemento] += 1
        if frecuencias[elemento] > max_frecuencia:
            moda = elemento
            max_frecuencia = frecuencias[elemento]
    return moda





def mediana(lista):
    n = len(lista)
    lista_ordenada = ascendenteLista(lista)

    if n % 2 == 0:
        mediana = (lista_ordenada[n // 2 - 1] + lista_ordenada[n // 2]) / 2
    else:
        mediana = lista_ordenada[n // 2]

    return mediana




print("la suma de la lista es",sumaLista(l1))
print("El promedio de la lista es",round(promedioLista(l1),2))
print("El numero mayor es",mayornum(l1))
print("El numero menor es",menornum(l1))
print("El numero ascendente es",ascendenteLista(l1))
print("El numero decendente es",decendente(l1))
print("La moda de la lista es",moda(l1))
print("La mediana de la lista es",mediana(l1))