import numpy as np
import csv
from ClaseFlores import Flores
class ManejadorFlores:
    __cantidad = 0
    __dimension = 0
    __incremento = 5


    def __init__(self, dimension=5, incremento=5):
        self.__flores = np.empty(dimension, dtype=Flores)
        self.__cantidad = 0
        self.__dimension = dimension

    def Cargar(self):
        archivo = open('flores.csv',encoding="utf-8")
        reader = csv.reader(archivo,delimiter=',')
        for linea in reader:
          flor = Flores(linea[0],linea[1],linea[2],linea[3])
          self.agregarFlor(flor)
        archivo.close()


    def agregarFlor(self, flor):
        if self.__cantidad == self.__dimension:
            self.__dimension += self.__incremento
            self.__flores.resize(self.__dimension)
        self.__flores[self.__cantidad] = flor
        self.__cantidad += 1

    def retornar(self,numero):
        return self.__flores[numero-1]



