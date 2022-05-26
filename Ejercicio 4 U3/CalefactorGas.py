from Calefactores import Calefactor
class CalefactorGas(Calefactor):
    __Matricula = None
    __Calorias = None

    def __init__(self,marca,modelo,matricula,calorias):
        super().__init__(marca,modelo)
        self.__Matricula == matricula
        self.__Calorias = calorias

    def getmatricula(self):
        return self.__Matricula
    def setmatricula(self,matri):
        self.__Matricula = matri

    def __str__(self):
        s = str(self.getmarca()) + '  '+ str(self.getmodelo()) +'  ' + str(self.__Calorias)+ '  ' + str(self.__Matricula)
        return str(s)

    def menorcosto(self,costo,cantidad):
        cos= (int(self.__Calorias)/1000)*int(cantidad)*int(costo)
        return int(cos)