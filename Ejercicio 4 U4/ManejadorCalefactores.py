import numpy as np
import csv
from Calefactores import Calefactor
from  CalefactorGas import  CalefactorGas
from CalefactorElectrico import  CalefactorElectrico
class ManejaCalefactor:
    __cantidad = 0
    __dimension = 0
    __incremento = 5

    def __init__(self, dimension, incremento=5):
        self.__Calefactor = np.empty(dimension, dtype=Calefactor)
        self.__cantidad = 0
        self.__dimension = dimension

    def agregarcalefactor(self, calefactor):
        if self.__cantidad == self.__dimension:
            self.__dimension += self.__incremento
            self.__Calefactor.resize(self.__dimension)
        self.__Calefactor[self.__cantidad] = calefactor
        self.__cantidad += 1

    def cargar(self):
        archivo= open("calefactor-a-gas.csv", encoding="utf-8" )
        reader = csv.reader(archivo,delimiter=",")
        for linea in reader:
            calefactor = CalefactorGas(linea[0],linea[1],linea[2],linea[3])
            self.agregarcalefactor(calefactor)
        archivo.close()
        archivo = open("calefactor-electrico.csv", encoding="utf-8")
        reader = csv.reader(archivo,delimiter=",")
        for linea in reader:
            calefactor = CalefactorElectrico(linea[0],linea[1],linea[2])
            self.agregarcalefactor(calefactor)
        archivo.close()

    def mostrar(self):
        for i in range(self.__cantidad):
            print(self.__Calefactor[i])