from cuenta import * 
from libro import *

class usuario:
    def __init__(self, nombre, id,):
        self.__nombre = nombre
        self.__id = id
        self.__librosReservados = []
        self.__librosDevueltos = []
        self.__multa=0
        cuenta.__init__(self.__librosReservados, self.__librosDevueltos)
        libros.__init__(self.__librosReservados, )

        def verificar (self, nombre_usuario):
            return nombre_usuario ==self.__id 
        
        def checar_cuenta (self, nombre, documento):
            if usuario.verificar (self, nombre, documento ) == 'verificador':
                self.__reservados.append (input("Digita el titulo reservado"))
                self.__devueltos.append (input("Digita el titulo devuelto"))
                periodo = int(input("Digita el numero de libros que se ha perdido"))
                librosPerdidos = cuenta.setlibros_perdidos 
                obj1 = cuenta (self.__librosReservados, self.__librosDevueltos)
                self.__reservados, self.__devueltos, self.__multa
                self.__multa= obj1.calculate_fine (librosPerdidos)
                return self.__reservados, self.__devueltos, self.__multa

        def infor_libro(self):
            print("Información del libro:")
            print("Título:", self.titulo)
            print("Autor:", self.autor)
            print("Publicación:", self.publicacion)
            print("ID:", self.id)

# Ejemplo de uso

def getusuario(self):
    return self.usuario       


class persona(usuario):
    def __init__(self,nombre, id,departamento):
        super().__init__(nombre, id,)
        self.departamento = departamento
    
    def saludo(self):
        return print(f"Holaa mi nombre es{self.nombre}\n mi id es {self.id}\n mi departamento es {self.departamento}")
    

def getpersona(self):
    return self.persona 

class estudiante(usuario):
    def __init__(self,nombre, id, clase):
        super().__init__(nombre, id)
        self.clase = clase
        
    def getestudiante(self):
        return self.estudiante

    def saludo1(self):
        return print(f"Holaa mi nombre es{self.nombre}\n mi id es {self.id}\n mi curso es {self.clase}")
    






