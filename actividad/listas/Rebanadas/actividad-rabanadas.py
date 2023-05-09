import random 
""" Llenar un arreglo de n elementos con números generados con la función random. No
puede haber números repetidos. Si intenta ingresar al arreglo un número que ya existe,
imprimirlo para anunciar que ese número ya está en el arreglo."""
n = int( random.randint(20,30))  
arr = []

while len(arr) < n:
    num = random.randint(1, 100)  # Generar un número aleatorio
    if num not in arr:  # Si el número no está en el arreglo, agregarlo
        arr.append(num)
    else:
        print(f"El número {num} ya está en el arreglo.")

print(arr)

