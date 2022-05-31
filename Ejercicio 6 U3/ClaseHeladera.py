from ClaseAparato import Aparato
import json
from pathlib import Path
class Heladera(Aparato):
    __capacidad = None
    __freezer = bool
    __ciclica = bool

    def __init__(self, marca, modelo, color, pais, precio,capacidad,freezer,ciclicla):
        super().__init__(marca, modelo, color, pais, precio)
        self.__capacidad = capacidad 
        self.__freezer = freezer
        self.__ciclica = ciclicla

    def toJSON(self):
        d = dict(
            __class__=self.__class__.__name__,
            __atributos__=dict(
                marca=self.getmarca(),
                modelo=self.getmodelo(),
                color=self.getcolor(),
                pais=self.getpais(),
                precio=self.getprecio(),
                capacidad=self.__capacidad,
                freezer=self.__freezer,
                ciclica=self.__ciclica
            )
        )
        return d

    def ImporteVenta(self):
        print('a')

    def __str__(self):
        return str(self.__capacidad)