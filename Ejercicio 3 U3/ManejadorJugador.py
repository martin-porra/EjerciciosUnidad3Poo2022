import datetime

from ClaseJugador import Jugador
import datetime
class ManejadorJugador:
    __lista = None

    def __init__(self):
        self.__lista = []

    def crearjugador(self):
        nombre = input('Ingresar nombre ')
        dni = input('Ingresar dni ')
        ciudad= input('Ingresar ciudad natal ')
        pais= input('Ingresar pais de origen')
        print('ingresar fecha de nacimiento ')
        dia= input('dia ')
        mes = input('mes ')
        año = input('año ')
        fechanacimiento= datetime.date(int(año),int(mes),int(dia))
        jugador = Jugador(nombre,dni,ciudad,pais,fechanacimiento)
        self.agregarJugador(jugador)

    def listar(self):
        for i in range(len(self.__lista)):
            print(i, '--->' ,  self.__lista[i])

    def agregarJugador(self,jugador):
        self.__lista.append(jugador)

    def getlista(self):
        return self.__lista




