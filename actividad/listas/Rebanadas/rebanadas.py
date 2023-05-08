"""llenar una lista con numeros aleatorios (reales) que representen calificaciones de un curso.Se evalua de 0 a 5.
El curso puede tener entre 20 y 30 aprendices.

Hallar
1. Saque lista nuevas para los aprobados y los reprobados( se aprueba con 3)
2. Genere lista nueva por cada unidad. Es decir, los que saque de 0 a 1 son un grupo, de 1 a 2 otro grupo y asi sucesivamente
3. Diga cual es el promedio de los que aprueban y de los que reprueban por separado"""

import random 
tam=int( random.randint(20,30))
lista =[float(random.randrange)(0,5) for i in range (tam)]
print(lista)

