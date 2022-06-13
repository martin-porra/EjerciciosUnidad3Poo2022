class Repartidor:
    __Identificador = None
    __Apellido = None
    __Nombre = None
    __Telefono = None
    __TipoMovilidad = None
    __ImporteComision = None

    def __init__(self,identificador,apellido,nombre,telefono,tipoM,importe=0):
        self.__Identificador = identificador
        self.__Apellido = apellido
        self.__Nombre = nombre
        self.__Telefono = telefono
        self.__TipoMovilidad = tipoM
        self.__ImporteComision =importe

    def getIdentificador(self):
        return self.__Identificador
    def getnombre(self):
        return self.__Nombre
    def getapellido(self):
        return self.__Apellido
    def gettelefono(self):
        return self.__Telefono
    def __str__(self):
        s = 'Apellido= ' + self.__Apellido + ' Nombre: ' + self.__Nombre + '\n' + 'Telefono: ' + self.__Telefono + ' Tipo Movilidad: '+ self.__TipoMovilidad
        return s
    def setcomision(self,comi):
        self.__ImporteComision = comi
    def __eq__(self, other):
        bandera = False
        if self.__Nombre == other.getnombre():
            if self.__Apellido == other.getapellido():
                if self.__Telefono == other.gettelefono():
                    bandera = True
                else:
                    bandera = False
            else:
                bandera = False
        else:
            bandera = False
        return bandera

    def getcomision(self):
        return int(self.__ImporteComision)
    def __gt__(self, other):
        bandera = False
        if int(self.__ImporteComision) > other.getcomision():
            bandera = True
        else:
            bandera = False
        return bandera
