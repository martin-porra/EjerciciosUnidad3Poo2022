import numpy as np
from ClaseEquipo import Equipo
import csv
class ManejaEquipos:
    __cantidad = 0
    __dimension = 0
    __incremento = 5

    def __init__(self, dimension=5, incremento=5):
        self.__Equipos = np.empty(dimension, dtype=Equipo)
        self.__cantidad = 0
        self.__dimension = dimension

    def Cargar(self):
        archivo = open('Equipos.csv', encoding="utf-8")
        reader = csv.reader(archivo, delimiter=',')
        for linea in reader:
            equipo = Equipo(linea[0], linea[1],linea[2])
            self.agregarequipo(equipo)
        archivo.close()

    def agregarequipo(self, equipos):
        if self.__cantidad == self.__dimension:
            self.__dimension += self.__incremento
            self.__Equipos.resize(self.__dimension)
        self.__Equipos[self.__cantidad] = equipos
        self.__cantidad += 1


    def __str__(self):
        s = ''
        i = 0
        for i in range(self.__cantidad):
            s+= str(i)+ '  ' + str(self.__Equipos[i].getNombre()) +  '   '+ str(self.__Equipos[i].getCiudad()) +'\n'
        return s

    def getlista(self):
        return self.__Equipos