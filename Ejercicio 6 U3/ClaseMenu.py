import os
from Manejador import  Manejador
from ClaseLavaropa import  Lavaropa
class Menu:

    def __init__(self):
      os.system('cls')

    def Menu(self):
     print("Selecciona una opción")
     print("\t1 - Agregar Elemento")
     print("\t2 - Insertar Elemento")
     print("\t3 - Calefactor de menor costo")
     print("\t4 - salir")

    def opcion(self, manejador):
     bandera = True
     while bandera == True:
      self.Menu()
      op = input("inserta un numero valor >> ")
      if op == "1":
       aparato = manejador.crearaparato()
       manejador.agregarElemento(aparato)
      elif op == "2":
       #aparato = manejador.crearaparato()
       lava = Lavaropa('hola','era','plan','pais','precio','capacidad','velocidad','cantidad','tipocarga')
       manejador.insertarElemento(lava)
      elif op == "3":
         manejador.mostrarDatos()
      elif op == "4":
          posicion = int(input('Ingresar posicion '))
          manejador.mostrarElemento(posicion)

      elif op == "5":
          bandera = False
      else:
       input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")