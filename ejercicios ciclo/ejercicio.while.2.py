# Solicitar dos números al usuario
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))

# Determinar el mayor y el menor número
if num1 > num2:
 mayor = num1
 menor = num2
else:
 
 mayor = num2
 menor = num1

# Calcular el cociente y el residuo sin utilizar la división ni el mod
cociente = 0
while mayor >= menor:
 mayor -= menor
 cociente += 1
residuo = mayor

print("El cociente del mayor número en el menor es:", cociente)
print("El residuo del mayor número en el menor es:", residuo)
