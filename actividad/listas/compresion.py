import random
rep=0
pos=[]
#Creamos lista con numeros aleatorios forma compresion 
lista =[int( random.randint(0,9)) for i in range(random.randrange(15,20))]
print(lista)

num=int(input("ingrese un numero"))

if num in lista:
    print(f"El numero {num} si esta")
else:
    print(f"El numero {num} no esta") 

for i in range (len(lista)):
         
    if num == lista[i]:
        pos.append(i)
print("El numero esta en la posicion",pos)
