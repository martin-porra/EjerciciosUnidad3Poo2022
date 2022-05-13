import csv
from claseFacultad import Facultad
from claseCarrera import Carrera

class manejadorFacultad:
    __listaFacultad = None

    def __init__(self):
        self.__listaFacultad = []

    def agregarFacultad(self, unaFacultad):
        if isinstance(unaFacultad, Facultad):
            self.__listaFacultad.append(unaFacultad)

    def leerArchivo(self):
        archivo = open('Facultades.csv',encoding="utf-8")
        reader = csv.reader(archivo, delimiter = ',')
        bandera = False
        for fila in reader:
            if not fila[1].isdigit():
                unaFacultad = Facultad(int(fila[0]),fila[1],fila[2],fila[3],fila[4])
                bandera = True
                
            else:  
                UnaCarrera = Carrera(int(fila[1]),fila[2],fila[3],fila[4])
                unaFacultad.agregarCarrera(UnaCarrera)
                
            if bandera == True:
                self.agregarFacultad(unaFacultad) 
                bandera =False
        archivo.close()

    def __str__(self):
        i = 0
        s = ''
        while i < len(self.__listaFacultad):
            s+=str(self.__listaFacultad[i])+'\n'
            i+=1
        return s    

    def Codigo(self):

            bandera = True
            while bandera == True:
             try:
                print('Ingresar codigo de una facultad')
                codigo = int(input())
                if type(codigo) == int:
                     bandera= False
                else:
                    codigo = int(input())
             except:
              print('debe ingresar un numero entero')
            i = 0
            bande = True
            bandera2 = False
            while i < len(self.__listaFacultad) and bande == True:
                if self.__listaFacultad[i].getCodigo() == codigo:
                    print(self.__listaFacultad[i].getNombre())
                    print('Carreras                                  Duracion:')
                    for o in range(len(self.__listaFacultad[i].getCarreras())):
                        print(self.__listaFacultad[i].getCarreras()[o].getNombre(),'                  ',self.__listaFacultad[i].getCarreras()[o].getDuracion() )
                    bande = False
                    bandera2 = True
                else:
                   i+=1
            if bandera2 == False:
                print('No se encontro codigo de facultad')

    def NombreCarrera(self):
        print('ingrese nombre de una carrera')
        carrera = input()
        bandera1 = True
        bandera2 = False
        i = 0
        while bandera1 == True and i < len(self.__listaFacultad):
            for o in range(len(self.__listaFacultad[i].getCarreras())):
                if self.__listaFacultad[i].getCarreras()[o].getNombre().lower() == carrera.lower():
                    print('Codigo carrera',self.__listaFacultad[i].getCodigo(),',',self.__listaFacultad[i].getCarreras()[o].getCodigo())
                    print('Nombre:',self.__listaFacultad[i].getNombre(),' --localidad de la facultad:',  self.__listaFacultad[i].getLocalidad())
                    bandera1 = False
                    bandera2 = True
            i+=1
        if bandera2 == False:
            print('No se encontro la carrera')

        



