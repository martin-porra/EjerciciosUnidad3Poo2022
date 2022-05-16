class Flores:
    __Numero = None
    __Nombre = None
    __Color = None
    __Descripcion = None

    def __init__(self,numero,nombre,color,descripcion):
        self.__Numero = numero
        self.__Nombre = nombre
        self.__Color = color
        self.__Descripcion = descripcion

    def getNumero(self):
        return self.__Numero
    def getNombre(self):
        return self.__Nombre

