# Definimos una función llamada "NumeroPerfecto" que toma un argumento llamado "num".
def NumeroPerfecto(num):
    suma=0

 # Creamos un bucle que itera desde 1 hasta num - 1.
    for i in range(1, num):
        if (num % (i) == 0):
           suma += (i)
    if num == suma:
         return True
    else:
         return False
 # Si la suma de todos los divisores de num (excluyendo num) es igual a num, entonces num es un número perfecto.
num = int(input("Digite numero:"))
if NumeroPerfecto(num):
    print(" es un numero perfecto", num)
else:
    print("No es un numero perfecto", num)