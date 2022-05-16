class Ramo:
    __Flores = None
    __Tamaño = None

    def __init__(self,tamaño):
        self.__Flores = []
        if tamaño <= 4 and tamaño > 0:
         self.__Tamaño = tamaño
        else:
            print('tamaño ingresado no permitido')

    def agregarflor(self,flor):
        self.__Flores.append(flor)

    def getFlores(self):
        i = 0
        s = ''
        for i in range(self.__Tamaño):
          s+= self.__Flores[i].getNombre() + '\n'
        return s

    def getFlor(self):
        return self.__Flores
    def getTamaño(self):
        return self.__Tamaño