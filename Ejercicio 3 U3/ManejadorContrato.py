import datetime

import numpy as np
from ClaseContrato import contrato
import csv
import  datetime as date

from ClaseJugador import Jugador
class ManejaContratos:
    __cantidad = 0
    __dimension = 0
    __incremento = 5

    def __init__(self, dimension=5, incremento=5):
        self.__Contratos = np.empty(dimension, dtype=contrato)
        self.__cantidad = 0
        self.__dimension = dimension

    def agregarcontrato(self, contrato):
        if self.__cantidad == self.__dimension:
            self.__dimension += self.__incremento
            self.__Contratos.resize(self.__dimension)
        self.__Contratos[self.__cantidad] = contrato
        self.__cantidad += 1

    def CrearContrato(self,jugador,equipo):
        from ClaseEquipo import Equipo
        fechain= date.date.today()
        print('Ingresar fecha de fin del contrato --- año/mes/dia')
        dia = int(input('dia '))
        mes = int(input('mes '))
        año = int(input('año '))
        fechafin = date.date(año,mes,dia)
        pago = input('ingresar pago mensual ')
        contra = contrato(fechain,fechafin,pago,jugador,equipo)
        self.agregarcontrato(contra)
        jugador.setcontrato(contra)
        equipo.setcontrato(contra)

    def ConsultarDni(self):
        dni = input('Ingresar dni de un jugador ')
        i=0
        for i in range(self.__cantidad):
          if int(dni) == int(self.__Contratos[i].getjugador().getdni()):
           print('Nombre equipo: ', self.__Contratos[i].getequipo().getnombre(),' Fecha finalizacion: ', self.__Contratos[i].getfechafin() )

    def identificadorequipo(self):
     iden = input('ingresar identificador de un equipo ')
     i=0
     fecha = datetime.date.today()
     for i in range(self.__cantidad):
        if int(iden) == int(self.__Contratos[i].getequipo().getnumero()):
            print(self.__Contratos[i].getfechafin().year)
            print(fecha.year)
            if (int(self.__Contratos[i].getfechafin().year) - int(fecha.year)) <= 0:
                print('a')
                if (int(self.__Contratos[i].getfechafin().month) - int(fecha.month))  < 6:
                    print(self.__Contratos[i].getjugador())

    def identificarnombre(self):
        nombre = input('ingresar nombre de un equipo ')
        i=0
        importe = 0
        for i in range(self.__cantidad):
            if self.__Contratos[i].getequipo().getnombre().lower() == nombre.lower():
              importe +=  int(self.__Contratos[i].getpago())
        print('el importe pagado por todos los contratos del club es: {}'.format(importe))
