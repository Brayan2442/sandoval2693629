class persona:
    def __init__(self,nombre,documento,curso):
        self.__nombre=nombre
        self.__documento=documento
        self.__curso=curso

    def setNombre(self,nombre):
            self.__nombre=nombre

    def getNombre(self):
            return self.__nombre
    
    def setDocumento(self,documento):
            self.__documento=documento

    def getDocumento(self):
            return self.__documento
    
    def setCurso(self,curso):
            self.__curso=curso

    def getCurso(self,):
            return self.__curso

cur=int(input('ingrese el curso'))         
curso=[801,802,803]
curso.append(cur)


if 10 in curso:
       curso.remove(-1)
print(curso)

