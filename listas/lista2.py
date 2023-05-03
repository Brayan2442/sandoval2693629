import random
lista=[]
suma = 0
resta = 0
tam=int(random.randint(10,20))
print(tam)
for i in range(tam):
    num=int(random.randrange(100))
    lista.append(num)

    suma+=num
    resta -= num
print(lista)

  

   

print(suma)
print(resta)

    