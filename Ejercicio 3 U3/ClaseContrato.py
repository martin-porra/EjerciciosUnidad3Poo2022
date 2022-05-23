class contrato:
    __fechainicio = None
    __fechadefin = None
    __pagoMensual = None
    __Jugador = None
    __Equipo = None

    def __init__(self,fechain,fechafin,pago,jugador,equipo):
        self.__fechainicio = fechain
        self.__fechadefin = fechafin
        self.__pagoMensual = pago
        self.__Equipo = equipo
        self.__Jugador = jugador
    def getjugador(self):
        return self.__Jugador
    def getequipo(self):
        return self.__Equipo
    def getfechafin(self):
        return self.__fechadefin
    def getpago(self):
        return self.__pagoMensual
