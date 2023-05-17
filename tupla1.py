#llenar una tupla con tamañp max 20 numeros entre 0 y 100 
tupla=()
import random
tam = int(random.randint(1,20))

for i in range(tam):
    num=int(random.randrange(100))
    tupla=tupla+(num,)
print(tupla)