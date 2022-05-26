from Calefactores import  Calefactor
class CalefactorElectrico(Calefactor):
    __PotenciaMaxima = None

    def __init__(self,marca,modelo,potencia):
        super().__init__(marca,modelo)
        self.__PotenciaMaxima = potencia

    def __str__(self):
        s = self.getmarca()+ ' '+ self.getmodelo()+' ' + self.__PotenciaMaxima
        return str(s)

    def menorcosto(self,costo,cantidad):
        cos= (int(self.__PotenciaMaxima)/1000)*int(cantidad)*int(costo)
        return int(cos)