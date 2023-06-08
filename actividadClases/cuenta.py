class cuenta:
    def __init__(self, librosPrestados, librosReservados, librosDevueltos, librosPerdidos, montoMulta): 
        self.__librosPrestados = librosPrestados
        self.__librosReservados = librosReservados
        self.__librosDevueltos = librosDevueltos
        self.__librosPerdidos = librosPerdidos
        self.__montoMulta = montoMulta
        
    def calculo(self):

        self.librosPrestados = int(input('Digite el numero de libros Prestados'))* 1000
        self.librosReservados = int(input('Digite el numero de libros reservados'))*500
        self.librosPerdidos = int(input('Digite el numero de libros perdidios'))*10000
        self.totalmulta = self.librosPrestados + self.librosReservados + self.librosPerdidos
        self.librosDevueltos = int(input('Digite el numero de libros devueltos'))
        self.total = self.totalmulta/self.librosDevueltos
        
