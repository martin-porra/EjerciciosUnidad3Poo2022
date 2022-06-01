import numpy as np
from ClaseContrato import contrato
import csv
from datetime import  datetime
from  datetime import  date
from ClaseJugador import Jugador
class ManejaContratos:
    __cantidad = 0
    __dimension = 0
    __incremento = 1

    def __init__(self, dimension=1, incremento=1):
        self.__Contratos = np.empty(dimension, dtype=contrato)
        self.__cantidad = 0
        self.__dimension = dimension

    def agregarcontrato(self, contrato):
        if self.__cantidad == self.__dimension:
            self.__dimension += self.__incremento
            self.__Contratos.resize(self.__dimension)
        self.__Contratos[self.__cantidad] = contrato
        self.__cantidad += 1
    def Mostrar(self):
        for contrato in self.__Contratos:
            print(contrato)

    def CrearContrato(self,jugador,equipo):
        from ClaseEquipo import Equipo
        fechain= datetime.today()
        fechai= str(fechain.date())
        print('Ingresar fecha de fin del contrato --- año/mes/dia')
        dia = input('dia ')
        mes = input('mes ')
        año = input('año ')
        fechafin = dia+'/'+mes+'/'+año
        pago = input('ingresar pago mensual ')
        contra = contrato(fechai,fechafin,pago,jugador,equipo)
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
     fechahoy = datetime.today()
     for i in range(self.__cantidad):
        if int(iden) == int(self.__Contratos[i].getequipo().getnumero()):
            fecha = datetime.strptime(self.__Contratos[i].getfechafin(), '%d/%m/%Y')
            if (int(fecha.year) - int(fechahoy.year)) <= 0:
                if (int(fecha.month) - int(fechahoy.month))  < 6:
                    print(self.__Contratos[i].getjugador())

    def identificarnombre(self):
        nombre = input('ingresar nombre de un equipo ')
        i=0
        importe = 0
        for i in range(self.__cantidad):
            if self.__Contratos[i].getequipo().getnombre().lower() == nombre.lower():
              importe +=  int(self.__Contratos[i].getpago())
        print('el importe pagado por todos los contratos del club es: {}'.format(importe))

    def guardarJSON(self):
        listaJSON = [contrato.toJSON() for contrato in self.__Contratos]
        return listaJSON
