import os
from ManejadorCalefactores import  ManejaCalefactor
from Calefactores import Calefactor
class Menu:

    def __init__(self):
      os.system('cls')

    def Menu(self):
     print("Selecciona una opción")
     print("\t1 - Calefon a gas de menor costo")
     print("\t2 - Calefon electrico a menor costo")
     print("\t3 - Calefactor de menor costo")
     print("\t4 - salir")

    def opcion(self, manejador):
     bandera = True
     while bandera == True:
      self.Menu()
      op = input("inserta un numero valor >> ")
      if op == "1":
       costogas = input('ingresar costo por m3 ')
       cantidadgas = input('ingresar cantidad que se estima consumir m3 ')
       calefactorgas = manejador.MenorCostoGas(costogas,cantidadgas)
       print('el calefactor a gas de menor consumo es \n Marca: {marca}  Modelo {modelo} '.format(
           marca=calefactorgas.getmarca(), modelo=calefactorgas.getmodelo()))
      elif op == "2":
       costoele = input('ingresar costo de kilowatt/h ')
       cantidadele = input('ingresar cantidad que se estima consumir por hora ')
       calefactorelectrico = manejador.MenorCostoElectrico(costoele,cantidadele)
       print('el calefactor electrico de menor consumo es \n Marca: {marca}  Modelo {modelo} '.format(
           marca=calefactorelectrico.getmarca(), modelo=calefactorelectrico.getmodelo()))
      elif op == "3":
          manejador.menorcosto(calefactorgas,calefactorelectrico,costogas,cantidadgas,costoele,cantidadele)
      elif op == "4":
          bandera = False
      else:
       input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")