import random

n = 10  
a = [random.randint(1, 10)]  

while len(a) < n:
    # Generar un número aleatorio mayor que el anterior y que no exceda la siguiente decena
    num = random.randint(a[-1] + 1, min(a[-1] + 10 - (a[-1] % 10), 100))
    a.append(num)

print(a)