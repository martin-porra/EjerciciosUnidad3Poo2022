class Calefactor:
    __Marca = None
    __Modelo = None

    def __init__(self,marca,modelo):
        self.__Marca = marca
        self.__Modelo = modelo

    def getmarca(self):
        return self.__Marca
    def getmodelo(self):
        return self.__Modelo
    def __str__(self):
        pass
    def menorcosto(self):
        pass
