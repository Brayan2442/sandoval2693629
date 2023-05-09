import random

n = 10  
arr = [random.randint(1, 10)]  

while len(arr) < n:
    # Generar un número aleatorio mayor que el anterior y que no exceda la siguiente decena
    num = random.randint(arr[-1] + 1, min(arr[-1] + 10 - (arr[-1] % 10), 100))
    arr.append(num)

print(arr)