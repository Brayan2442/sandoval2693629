# Se pide al usuario que ingrese un número entero positivo.
numero = int(input("Ingresa un número entero positivo: "))
# Se verifica si el número es mayor que 1.
if numero > 1:
    es_primo = True
 # Se inicializa la variable es_primo en Verdadero.
    for i in range(2, int(numero/2)+1):
        if numero % i == 0:
            es_primo = False
        break
    if es_primo: 
        print("El número", numero, "es primo.")
# Si es_primo es Falso, entonces el número no es primo.
    else:
        print("El número", numero, "no es primo.")
else:
  print("El número ingresado no es válido.")