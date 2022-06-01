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
    def __str__(self):
        return str(self.__pagoMensual)
    def toJSON(self):
        d = dict(
            __class__=self.__class__.__name__,
            __atributos__=dict(
                DNI=self.__Jugador.getdni(),
                Nombre_Equipo=self.__Equipo.getnombre(),
                fechainicio=self.__fechainicio,
                fechafin=self.__fechadefin,
                pagomensual=self.__pagoMensual,
            )
        )
        return d

