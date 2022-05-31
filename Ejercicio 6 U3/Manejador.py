from ClaseLista import Lista
from  ClaseAparato import Aparato
from ClaseTelevisor  import Televisor
from ClaseLavaropa import  Lavaropa
from ClaseHeladera import  Heladera
class Manejador:
     __lista = None

     def __init__(self):
         self.__lista = Lista()

     def agregarAparato(self, unAparato):
        self.__lista.agregarAparato(unAparato)

     def mostrarDatos(self):
        for dato in self.__lista:
            print(dato)

     def toJSON(self):
        d = dict(
            __class__=self.__class__.__name__,
            aparatos=[Aparato.toJSON() for Aparato in self.__lista]
            )
        return d


     def crearaparato(self):
         op = input('1 ------ Heladera \n2 ------ Televisor \n3 ------- Lavaropa\n')

         if int(op) == 1:
             print('Ingresar datos de Heladera')
             marca = input('Marca ')
             modelo = input('Modelo ')
             color = input('Color ')
             pais = input('Pais ')
             precio = input('Precio ')
             capacidad = input('Capacidad ')
             freezer = input('Freezer ')
             ciclica = input('Ciclica ')
             heladera = Heladera(marca, modelo, color, pais, precio, capacidad, freezer, ciclica)
             aparato = heladera
         elif int(op) == 2:
             print('Ingresar datos de Televisor')
             marca = input('Marca ')
             modelo = input('Modelo ')
             color = input('Color ')
             pais = input('Pais ')
             precio = input('Precio ')
             tipo = input('Tipo ')
             pulgadas = input('Pulgadas ')
             definicion = input('Definicion ')
             conexion = input('conexion ')
             televisor = Televisor(marca, modelo, color, pais, precio, tipo, pulgadas, definicion, conexion)
             aparato = televisor
         elif int(op) == 3:
             print('Ingresar datos del lavarropas')
             marca = input('Marca ')
             modelo = input('Modelo ')
             color = input('Color ')
             pais = input('Pais ')
             precio = input('Precio ')
             capacidad = input('Capacidad ')
             velocidad = input('Velocidad ')
             cantidad = input('Cantidad ')
             tipocarga = input('Tipo Carga ')
             lavaropas = Lavaropa(marca, modelo, color, pais, precio, capacidad, velocidad, cantidad, tipocarga)
             aparato = lavaropas
         else:
             print('Opcion incorrecta')
         return aparato

     def agregarElemento(self,aparato):
             self.__lista.agregarElemento(aparato)

     def insertarElemento(self,aparato):
         pos = int(input('Ingresar posicion donde insertara el elemento '))
         self.__lista.insertarElemento(aparato,pos)

     def mostrarElemento(self,posicion):
         self.__lista.mostrarElemento(posicion)

     def Aparatosphillips(self):
         cont = 0
         for dato in self.__lista:
             if dato.getmarca().lower() == 'phillips':
                 cont +=1
         print(cont)

