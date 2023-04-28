#codigo que diga los multiplos que haya en la serie
n = int(input("Ingrese numero inicial: "))
end = int(input("ingrese numero final: "))
count = int(input("ingrese numero de incremento o decremento"))

for i in range(0, end+1, n):
    count += 1

print("Hay", count, "Multiplos de", n, "en la serie.")