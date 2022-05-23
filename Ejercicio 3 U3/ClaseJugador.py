class Jugador:
    __Nombre = None
    __DNI = None
    __CiudadNatal= None
    __PaisDeOrigen = None
    __FechaNacimiento = None
    __Contratos = None

    def __init__(self,nombre,dni,ciudad,paises,fecha):
        self.__Nombre = nombre
        self.__DNI = dni
        self.__CiudadNatal = ciudad
        self.__PaisDeOrigen = paises
        self.__FechaNacimiento = fecha
        self.__Contratos = []
    def setcontrato(self,contrato):
        self.__Contratos.append(contrato)

    def getdni(self):
        return self.__DNI
    def __str__(self):
        s = str(self.__DNI) + '  ' + str(self.__Nombre)+ '  '+ str(self.__CiudadNatal)+ ' '+  str(self.__PaisDeOrigen)
        return  str(s)