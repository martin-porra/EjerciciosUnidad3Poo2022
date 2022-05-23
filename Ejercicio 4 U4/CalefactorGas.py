from Calefactores import Calefactor
class CalefactorGas(Calefactor):
    __Matricula = None
    __Calorias = None

    def __init__(self,marca,modelo,matricula,calorias):
        super().__init__(marca,modelo)
        self.__Matricula == matricula
        self.__Calorias = calorias

    def __str__(self):
        s = str(self.getmarca()) + '  '+ str(self.getmodelo()) +'  ' + str(self.__Calorias)+ '  ' + str(self.__Matricula)
        return str(s)