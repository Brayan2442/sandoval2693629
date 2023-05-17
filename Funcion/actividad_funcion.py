import random

def llenarLista(tam, rango):
    # Creamos una lista con números aleatorios
    lista = [random.randrange(rango) for _ in range(tam)]
    return lista

def sumaLista(lista):
    # Creamos una variable suma
    sumatoria = 0
    # Hacemos un ciclo for
    for x in lista:
        sumatoria += x
    return sumatoria

l1 = llenarLista(8, 10)
print(l1)

l2 = llenarLista(4, 10)
print(l2)

suma_l1 = sumaLista(l1)
suma_l2 = sumaLista(l2)

print("La suma de la primera lista es:", suma_l1)
print("La suma de la segunda lista es:", suma_l2)



def mayorLista(lista):
    # Buscamos el número máximo en la lista
    mayor = (lista)
    return mayor


mayor_l1 = l1[0]
mayor_l2 = l2[0]

for num in l1:
    if num > mayor_l1:
        mayor_l1 = num

for num in l2:
    if num > mayor_l2:
        mayor_l2 = num

print("El número mas grande en la primera lista es:", mayor_l1)
print("El número mas grande en la segunda lista es:", mayor_l2)

if mayor_l1 > mayor_l2:
    print("La lista 1 tiene el número máximo más alto.")
elif mayor_l1 < mayor_l2:
    print("La lista 2 tiene el número máximo más alto.")


def menorLista(lista):
    # Buscamos el número máximo en la lista
    menor1 = (lista)
    return menor1

def menorLista(lista):
    # Buscamos el número máximo en la lista
    menor2 = (lista)
    return menor2


menor1 = l1[0]
menor2 = l2[0]

for num in l1:
    if num < menor1:
        menor1 = num

for num in l2:
    if num < menor2:
        menor2 = num

print("El número mas pequeño en la primera lista es:", menor1)
print("El número mas pequeño en la segunda lista es:", menor2)

if menor1 > menor2:
    print("La lista 1 tiene el mas pequeño.")
elif menor1 > menor2:
    print("La lista 2 tiene el número máximo más alto.")


def promedioLista(lista):
    # Calculamos el promedio de los elementos de la lista
    promedio = sum(lista) / len(lista)
    return promedio


promedio_l1 = promedioLista(l1)
promedio_l2 = promedioLista(l2)

print("El promedio de la primera lista es:", promedio_l1)
print("El promedio de la segunda lista es:", promedio_l2)

def listaunida(lista1,lista2):
    lista1.e
    
lista2 = [(suma_l1+suma_l2)/len()]
print(lista2)

