from ClaseLista import Lista
from  ClaseAparato import Aparato
class Manejador:
     __lista = None

     def __init__(self):
         self.__lista = Lista()

     def agregarAparato(self, unAparato):
        self.__lista.agregarAparato(unAparato)

     def mostrarDatos(self):
        for i in range(len(self.__lista)):
            print(self.__lista[i])

     def toJSON(self):
        d = dict(
            __class__=self.__class__.__name__,
            aparatos=[Aparato.toJSON() for Aparato in self.__lista]
            )
        return d