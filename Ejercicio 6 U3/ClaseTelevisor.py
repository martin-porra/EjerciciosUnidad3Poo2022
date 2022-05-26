from ClaseAparato import Aparato
import json
from pathlib import Path
class Televisor(Aparato):
    __tipopantalla =None
    __pulgadas = None
    __TipoDefinicion= None
    __Conexion = bool


    def __init__(self, marca, modelo, color, pais, precio,tipo,pulgadas,definicion,conexion):
        super().__init__(marca, modelo, color, pais, precio)
        self.__tipopantalla = tipo
        self.__pulgadas = pulgadas
        self.__TipoDefinicion = definicion
        self.__Conexion = conexion

    def toJSON(self):
        d = dict(
            __class__=self.__class__.__name__,
            __atributos__=dict(
                marca=self.getmarca(),
                modelo=self.getmodelo(),
                color=self.getcolor(),
                pais=self.getpais(),
                precio=self.getprecio(),
                tipo=self.__tipopantalla,
                pulgadas=self.__pulgadas,
                definicion=self.__TipoDefinicion,
                conexion=self.__Conexion
            )
        )
        return d