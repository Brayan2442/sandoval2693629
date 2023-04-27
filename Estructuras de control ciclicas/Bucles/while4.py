# Leer dos números
num1 = int(input("Introduce el primer número: "))
num2 = int(input("Introduce el segundo número: "))

# Garantizar que hay uno mayor que el otro
while num1 == num2:
    print("Los números son iguales. Por favor, introdúcelos de nuevo.")
    num1 = int(input("Introduce el primer número: "))
    num2 = int(input("Introduce el segundo número: "))

if num1 > num2:
    mayor = num1
    menor = num2
else:
    mayor = num2
    menor = num1

# Restar el menor del mayor y, si es posible, restar de nuevo
resultado = mayor - menor
if resultado >= menor:
    resultado -= menor

# Mostrar el resultado
print(f"El resultado es {resultado}")