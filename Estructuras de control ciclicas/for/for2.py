#codigo que diga los multiplos que haya en la serie
n = int(input("Ingrese numero positivo: "))
end = int(input("ingrese numero final: "))
count = 0

for i in range(0, end+1, n):
    count += 1

print("Hay", count, "Multiplos de", n, "en la serie.")