# Inicializar el resultado con 1
resultado = 1
x=0
n=0
# Calcular la operación x^n s
if n > 0:
    i = 1
    while i <= n:
        resultado *= x
        i += 1
elif n < 0:
    i = 1
    while i <= abs(n):
        resultado /= x
        i += 1
else:
    resultado = 1

print("El resultado de la operación", x, "^", n, "es:", resultado)