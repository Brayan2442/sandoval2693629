import random

def numnat(x):
    suma= 0
    n=1 
    while suma < maximo:
        n=n+suma 
    return n-1 

maximo = int(input("Introduce un numero maximo:"))
lista = numnat(-1)
print("El numero natural mas pequeño necesario para superar el maximo:", lista)