class Pedido:
    __IdentificadorRepartidor = None
    __NumeroPedido = None
    __Descripcion = None
    __Cantidad= None
    __PrecioUnitario = None
    __EstadoPedido = None

    def __init__(self,identificador,numero,descripcion,cantidad,precio,estado):
        self.__IdentificadorRepartidor = identificador
        self.__NumeroPedido = numero
        self.__Descripcion = descripcion
        self.__Cantidad = cantidad
        self.__PrecioUnitario = precio
        self.__EstadoPedido = estado

    def getidentificador(self):
        return self.__IdentificadorRepartidor
    def getestado(self):
        return self.__EstadoPedido

    def __str__(self):
        s = str(self.__NumeroPedido) +'                '+ str(self.__Descripcion) +  '        '+ str(self.__Cantidad) + '        ' + str(self.__PrecioUnitario) + '          ' + str(int(self.__PrecioUnitario)*int(self.__Cantidad))
        return s
    def gettotal(self):
        total = int(self.__PrecioUnitario)*int(self.__Cantidad)
        return total