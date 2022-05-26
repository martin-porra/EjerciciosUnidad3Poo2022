from ClaseAparato import Aparato
import json
from pathlib import Path
class Lavaropa(Aparato):
    __capacidad = None
    __velocidad = None
    __cantidad = None
    __tipocarga  = None

    def __init__(self, marca, modelo, color, pais, precio,capacidad,velocidad,cantidad,tipocarga):
        super().__init__(marca, modelo, color, pais, precio)
        self.__capacidad = capacidad
        self.__velocidad = velocidad
        self.__cantidad = cantidad
        self.__tipocarga = tipocarga

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
                velocidad=self.__velocidad,
                cantidad=self.__capacidad,
                tipocarga=self.__tipocarga
            )
        )
        return d