from usuario import*
class persona(usuario):
    def __init__(self,nombre, id,departamento):
        super().__init__(nombre, id,)
        self.departamento = departamento
    
    def saludo(self):
        return print(f"Holaa mi nombre es{self.nombre}\n mi id es {self.id}\n mi departamento es {self.departamento}")
    
    def getpersona(self):
        return self.persona 