N = int(input("Ingrese un número: "))
multiplos_de_5 = []

i = 1
while i <= N:
     if i % 5 == 0:
        multiplos_de_5.append(i)
     i += 1

print("Los múltiplos de 5 comprendidos entre 1 y", N, "son:", multiplos_de_5)
 