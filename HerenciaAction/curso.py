class Curso:
    #creamos un constructor con parametros
    def __init__(self,nombre,tipo):
        self.__nombre=nombre
        self.__tipo=tipo
#Creamos una metodo para poder retornar el nombre
    def getNombre(self):
        return self.__nombre
    
# class Grado(Curso):
#     def __init__(self,nombre,tipo,semestre):
#         super(Grado,self).__init__(nombre,tipo)
#         self.__semestre=semestre

#     def saludo(self):
#         print(f"hola {self._Curso__nombre} de tipo {self._Curso__tipo} y del semestre {self._Grado__semestre}")

# ob1=Grado("melqui", "diurna", "2do")
# ob1.saludo()
