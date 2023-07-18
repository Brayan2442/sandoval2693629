import math
try: 
    a=int(input("ingrese el primer digito"))
    b=int(input("ingrese el primer digito"))
    c=int(input("ingrese el primer digito"))
except ValueError:
    print("Error: Debes ingresar solo números enteros")
except:
    print("Error con la ejecucion")

try:
    d= (b*b) -4*a*c 
except NameError:
     print("no se permite seguir con el programa")
try:
        if d<0:
             print('No existe solucion')
        else: 
          x1=(-b+math.sqrt(d))/(2*a)
          x2=(-b-math.sqrt(d))/(2*a)
except NameError:
        print(' no se puede seguir ejecutando el programa')
        print('solucion x1: ',x1)
        print('solucion x2: ',x2)

except:
    print ('No se puede terminar el programa')







def resolver_ecuacion_cuadratica(a, b, c):
    
    discriminante = b**2 - 4*a*c

    if discriminante < 0:
        return None
    else:
        x1 = (-b + math.sqrt(discriminante)) / (2 * a)
        x2 = (-b - math.sqrt(discriminante)) / (2 * a)
        return x1, x2

def main():
    try:
        a = float(input("Ingrese el coeficiente cuadrático (a): "))
        b = float(input("Ingrese el coeficiente lineal (b): "))
        c = float(input("Ingrese el término independiente (c): "))
    except ValueError:
        print("Error: Debe ingresar solo números válidos para los coeficientes.")
    else:
        soluciones = resolver_ecuacion_cuadratica(a, b, c)
        if soluciones is None:
            print("No hay soluciones reales para la ecuación cuadrática.")
        else:
            x1, x2 = soluciones
            print(f"Las soluciones de la ecuación son: x1 = {x1:.2f}, x2 = {x2:.2f}")

if __name__ == "__main__":
    main()
