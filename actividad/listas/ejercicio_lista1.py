#ejercicio con la ley de Fibonacci
n=int(input("ingrese un numero"))
lista=[]
a,b=0,1
while n>0:
    lista.append(a)
    a,b=b,a+b
    n-=1
print(lista)

