class Curso:
    #creamos un constructor con parametros
    def __init__(self,nombre,tipo):
        self.__nombre=nombre
        self.__tipo=tipo

    def getNombre(self):
        return self.__nombre