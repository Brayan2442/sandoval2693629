from persona import *
from curso import *
# creamos una subclase que aprendiz que proviene de la clase persona
class Aprendiz(Persona):
    #creamos un constructor
    def __init__(self,nombre,documento,formacion,ficha):
        Persona.__init__(self,nombre,documento)
        self.__formacion=formacion
        self.__ficha=ficha
        self.__cursos=[]
    # creamos un metodo que permite añadir cursos a la lista cursos
    def agregarCurso(self,curso):
        self.__cursos.append(curso)
    #Creamos un metodo para que pueda ingresar nombres y tipo de cursos a la lista
    def componerCurso(self):
        nombreCurso=input('Ingrese nombre del curso')
        tipoCurso=input('Ingrese tipo del curso')
        objcurso=Curso(nombreCurso,tipoCurso)
        self.__cursos.append(objcurso)
    #creamos metodo para permitir que vea los cursos
    def verCursos(self):
        return self.__cursos





















































































































    def agregarCurso(self,curso):
        self.__cursos.append(curso)
    
    def componerCurso(self):
        nombreCurso=input('Ingrese nombre del curso')
        tipoCurso=input('Ingrese tipo del curso')
        objcurso=Curso(nombreCurso,tipoCurso)
        self.__cursos.append(objcurso)
    
    def verCursos(self):
        return self.__cursos