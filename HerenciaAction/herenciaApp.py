from aprendiz import *
from curso import *
#Creamos un objeto donde esta almacenando a aprendiz y da a mostrar el nombre, numero de identidad, programa de formacion y ficha
objeto=Aprendiz("Ana Kurnikova",123456,'ADSO',2693629)
#print(objeto.__dict__)
#Creamos un objeto donde esta almacenando a curso donde tiene parametros
objcurso=Curso("Programacion Software","tecnico")
#Esta llamando un objeto que se llama objeto.agregarCurso 
objeto.agregarCurso(objcurso)
#print(objeto.__dict__)
#Esta llamando un objeto que se llama objeto.componerCurso
objeto.componerCurso()
objeto.componerCurso()
#print(objeto.verCursos())
for cursito in objeto.verCursos():
    print(cursito.getNombre())
