import random

lista = []
suma = 0
resta = 0
tam = int(random.randint(10, 20))

print(tam)

for i in range(tam):
    num = int(random.randrange(100))
    lista.append(num)
    suma += num

    if i == 0:
        mayor = num
        menor = num
    else:
        if num > mayor:
            mayor = num
        if num < menor:
            menor = num

# Calcular la media
media = suma / tam



print(lista)
print("La suma de los elementos de la lista es:", suma)
print("El porcentaje de la suma de los elementos de la lista es:", (suma / 1000) * 100, "%")
print("El número mayor es:", mayor)
print("El número menor es:", menor)
print("La media de la lista es:", media)
print("La moda de la lista es:", moda)

