from usuario import*
class estudiante(usuario):
    def __init__(self,nombre, id, clase):
        super().__init__(nombre, id)
        self.clase = clase
        
    def getestudiante(self):
        return self.estudiante

    def saludo1(self):
        return print(f"Holaa mi nombre es{self.nombre}\n mi id es {self.id}\n mi curso es {self.clase}")