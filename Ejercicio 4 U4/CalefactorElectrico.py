from Calefactores import  Calefactor
class CalefactorElectrico(Calefactor):
    __PotenciaMaxima = None

    def __init__(self,marca,modelo,potencia):
        super().__init__(marca,modelo)
        self.__PotenciaMaxima = potencia

    def __str__(self):
        s = self.getmarca()+ ' '+ self.getmodelo()+' ' + self.__PotenciaMaxima
        return str(s)