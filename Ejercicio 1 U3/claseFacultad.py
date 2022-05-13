from ast import Import
from claseCarrera import Carrera


from claseCarrera import Carrera

class Facultad:
    __Codigo = None
    __Nombre = None
    __Direccion = None
    __Localidad = None
    __Telefono = None
    __ListaCarrera = None

 
    def agregarCarrera(self, unaCarrera):
        if isinstance(unaCarrera, Carrera):
            self.__ListaCarrera.append(unaCarrera)

    def __init__(self, codigo = None, Nombre = None, direccion = None, localidad = None, telefono = None):
        self.__Codigo = codigo
        self.__Nombre = Nombre
        self.__Direccion = direccion
        self.__Localidad = localidad
        self.__Telefono = telefono
        self.__ListaCarrera = []

    def __str__(self):
        s = 'Codigo: {}, Nombre: {}, Direccion: {}, Localidad: {}, Telefono: {}\n'.format(self.__Codigo, self.__Nombre, self.__Direccion, self.__Localidad, self.__Telefono)
        s +='Carreras:\n'
        for carrera in self.__ListaCarrera:
            s+= str(carrera)+'\n'
        return s

    def getCodigo(self):
        return self.__Codigo

    def getNombre(self):
       return self.__Nombre
    def getCarreras(self):
        return self.__ListaCarrera
    def getLocalidad(self):
        return self.__Localidad
       


 

