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
            calefactor.setmatricula(linea[2])
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

    def MenorCostoGas(self,costo,cantidad):
        menor = 100000000
        i=0
        calefactor= None
        for i in range(self.__cantidad):
            if type(self.__Calefactor[i]) == CalefactorGas:
                cos = self.__Calefactor[i].menorcosto(costo,cantidad)
                if cos < menor:
                    menor = cos
                    calefactor= self.__Calefactor[i]
        return  calefactor

    def MenorCostoElectrico(self,costo,cantidad):
        menor = 100000000
        i=0
        calefactor= None
        for i in range(self.__cantidad):
            if type(self.__Calefactor[i]) == CalefactorElectrico:
                cos = self.__Calefactor[i].menorcosto(costo,cantidad)
                if cos < menor:
                    menor = cos
                    calefactor= self.__Calefactor[i]
        return calefactor

    def menorcosto(self,calefactorgas,calefactorelectrico,cost1,cant1,cost2,cant2):
         costo = calefactorgas.menorcosto(cost1,cant1)
         costo2 = calefactorelectrico.menorcosto(cost2,cant2)
         if costo > costo2:
             print('Calefactor a gas')
             print(calefactorgas)
         else:
             print('Calefactor electrico')
             print(calefactorelectrico)