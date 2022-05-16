import os
from ManejadorFlores import  ManejadorFlores
from ManejadoresRamos import  ManejadorRamos
class Menu:

    def __init__(self):
      os.system('cls')

    def Menu(self):
     print("Selecciona una opción")
     print("\t1 - Añadir Ramo")
     print("\t2 - Contar Flores vendidas")
     print("\t3 - Flores vendidas por tamaño de Ramos")
     print("\t4 - salir")

    def opcion(self, manejador,manejadorFlores):
     bandera = True
     while bandera == True:
      self.Menu()
      op = input("inserta un numero valor >> ")
      if op == "1":
       manejador.AñadirRamo(manejadorFlores)
      elif op == "2":
       manejador.Contar()
      elif op == "3":
          manejador.tipoRamo()
      elif op == "4":
          bandera = False
      else:
       input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")