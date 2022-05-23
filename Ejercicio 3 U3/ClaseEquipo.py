import datetime
from ClaseContrato import contrato
from ManejadorContrato import  ManejaContratos
import datetime as date
class Equipo:
    __numero = None
    __Nombre = None
    __Ciudad =  None
    __Contratos = None

    def __init__(self,numero,nombre,ciudad):
        self.__numero = numero
        self.__Ciudad = ciudad
        self.__Nombre = nombre
        self.__Contratos = []

    def getnombre(self):
        return self.__Nombre
    def getnumero(self):
        return self.__numero



    def getNombre(self):
        return self.__Nombre
    def getCiudad(self):
        return self.__Ciudad
    def setcontrato(self,contrato):
        self.__Contratos.append(contrato)