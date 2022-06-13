from ClasePedido import Pedido
import numpy as np
import csv

class ManejadorPedidos:
    __cantidad = 0
    __dimension = 0
    __incremento = 5

    def __init__(self, dimension=5, incremento=5):
        self.__pedidos = np.empty(dimension, dtype=Pedido)
        self.__cantidad = 0
        self.__dimension = dimension

    def Cargar(self):
        archivo = open('pedidos.csv')
        reader = csv.reader(archivo, delimiter=';')
        bandera = True
        for linea in reader:
            if bandera:
                bandera = False
            else:
                pedido = Pedido(linea[0], linea[1], linea[2], linea[3], linea[4], linea[5])
                self.agregarPedido(pedido)
        archivo.close()

    def PedidosPendientes(self):
        identificador = input('ingresar el identificador de un repartidor ')
        i = 0
        bandera = False
        print('Pedidos pendientes: ')
        for i in range(self.__cantidad):
            if identificador == self.__pedidos[i].getidentificador():
               if self.__pedidos[i].getestado() == 'N':
                   print(self.__pedidos[i])
                   bandera = True
        if bandera == False:
            print('No se encontro el repartidor con pedidos pendientes')

    def agregarPedido(self, pedido):
        if self.__cantidad == self.__dimension:
            self.__dimension += self.__incremento
            self.__pedidos.resize(self.__dimension)
        self.__pedidos[self.__cantidad] = pedido
        self.__cantidad += 1

    def mostrar(self):
        print(self.__pedidos)

    def getLista(self):
        return self.__pedidos
    def getcantidad(self):
        return self.__cantidad

