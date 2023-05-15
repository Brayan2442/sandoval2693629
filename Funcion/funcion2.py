import random
lista = []
tam = int(random.randint( 15, 125))

for i in range(tam):
    num = int(random.randrange(100))
    lista.append(num)
print("numeros",(lista))


