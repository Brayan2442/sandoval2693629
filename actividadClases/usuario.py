class usuario:
    def __init__(self, nombre, id,):
        self.nombre = nombre
        self.id = id

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
    






