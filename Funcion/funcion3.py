
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



def mayorLista(lista):
    
    mayor=max(lista)
    return mayor


def menorLista(lista):
    
    menor=min(lista)
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
    for i in range(len(lista)):
        





print(sumaLista(l1))
print(round(promedioLista(l1),2))
print(mayorLista(l1))
print(menorLista(l1))
print(ascendenteLista(l1))
print(decendente(l1))