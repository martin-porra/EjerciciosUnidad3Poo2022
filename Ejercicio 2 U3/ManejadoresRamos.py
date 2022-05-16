from ManejadorFlores import ManejadorFlores
from ClaseRamo import Ramo
class ManejadorRamos:
    __Lista = None

    def __init__(self):
        self.__Lista = []

    def AñadirRamo(self,ManejadorFlores):
        print('ingresar numeros de flores que quiere añadir al ramo, tiene que ser menor o igual a 4')

        numero = int(input())
        ramo = Ramo(numero)
        print('Las flores disponibles son: \n 1 --> violeta  \n 2 --> margaritas \n 3 --> azucenas\n 4 --> lirio \n 5 --> rosas \n Cuales desea añadir?')
        i=0
        for i in range(numero):
             flor= int(input())
             if flor > 0 and flor < 6:
                ramo.agregarflor(ManejadorFlores.retornar(flor))
        self.__Lista.append(ramo)

    def __str__(self):
        i = 0
        s = ''
        for i in range(len(self.__Lista)):
            s+=self.__Lista[i].getFlores() + '\n'
        return s


    def Contar(self):
        lista=[0,0,0,0,0]
        lista1=['violeta','margaritas','azucenas','lirio','rosas']
        i = 0
        o=0
        for i in range(len(self.__Lista)):
            for o in range(len(self.__Lista[i].getFlor())):
                if self.__Lista[i].getFlor()[o].getNombre()  == 'violeta':
                    lista[0]+=1
                elif self.__Lista[i].getFlor()[o].getNombre()  == 'margaritas':
                    lista[1] += 1
                elif self.__Lista[i].getFlor()[o].getNombre()  == 'azucenas':
                    lista[2] += 1
                elif self.__Lista[i].getFlor()[o].getNombre()  == 'lirio':
                    lista[3] += 1
                elif self.__Lista[i].getFlor()[o].getNombre()  == 'rosas':
                    lista[4] += 1
        i=0
        aux = 0
        for i in range(3):
         if lista[i] < lista[i+1]:
             lista1[i],lista1[i+1] =lista1[i+1], lista1[i]
             lista[i],lista[i+1] =lista[i+1], lista[i]
        print('Las flores mas pedidas en orden son:')
        o=0
        for o in range(len(lista)):
            print(lista1[o])
            print(lista[o])

    def tipoRamo(self):
        print('ingresar tamaño del Ramo')
        try:
            tamaño = int(input())
            if type(tamaño) == int:
                if tamaño > 0 and tamaño <=4:
                        lista = []
                        for i in range(len(self.__Lista)):
                            if self.__Lista[i].getTamaño() == tamaño:
                                for o in range(len(self.__Lista[i].getFlor())):
                                    if self.__Lista[i].getFlor()[o].getNombre() not in lista:
                                        lista.append(self.__Lista[i].getFlor()[o].getNombre())
                        print('El tipo de flores vendidas para los Ramos de tamaño {tam} son:'.format(tam=tamaño))
                        print(lista)
                else:
                    print('tamaño ingresado incorrecto')
            else:
                print('No es un entero')
        except:
            print('No es un entero')


