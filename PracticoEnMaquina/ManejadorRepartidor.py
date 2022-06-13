import  csv
from ClaseRepartidor import  Repartidor
from  ManejadorPedido import  ManejadorPedidos
class ManejadorRepartidores:
    __Lista = None

    def __init__(self):
        self.__Lista = []
        self.CargarLista()

    def CargarLista(self):
     archivo = open('repartidores.csv',encoding="utf-8")
     reader = csv.reader(archivo,delimiter=';')
     bandera = True
     for fila in reader:
         if bandera:
             bandera = False
         else:
            repartidor = Repartidor(fila[0],fila[1],fila[2],fila[3],fila[4],fila[5],)
            self.__Lista.append(repartidor)
     archivo.close()

    def getlista(self):
        return self.__Lista

    def PedidoEntregado(self, manejador):
        from ManejadorPedido import  ManejadorPedidos
        i = 0
        for i in range(len(self.__Lista)):
            print('-----------------------------')
            print(self.__Lista[i])
            print('Numero pedido        Descripcion             Cantidad  Precio Unitario  Total')
            bandera = False
            tota = 0
            for o in range(manejador.getcantidad()):
                if int(manejador.getLista()[o].getidentificador()) == int(i):

                    tota += manejador.getLista()[o].gettotal()
                    bandera = True
                    print(manejador.getLista()[o])
            if bandera == True:
             print('Total                                                                 ',tota)
             comision = (int(tota)*5/100)
             self.__Lista[i].setcomision(comision)
             print('Importe a pagar por comision: ',comision  )


    def iguales(self):
        print('ingresar el identificador de un repartidor ')
        repartidor = input()
        i = 0
        cant = 0
        for i in range(len(self.__Lista)):
            if self.__Lista[i] == self.__Lista[int(repartidor)-1]:
                cant +=1
        if cant > 1:
            print('Repartidor repetido se borrara')
            self.__Lista.pop(int(repartidor)-1)
        else:
            print('Repartidor no repetido')


    def ordenar(self):
        self.__Lista.sort(reverse=True)
        i = 0
        print('Listado de repartidores ordenados de mayor a menor')
        for i in range(len(self.__Lista)):
            print('Nombre: ' + str(self.__Lista[i].getnombre()) + ' Importe comision:  ' + str(self.__Lista[i].getcomision()))

