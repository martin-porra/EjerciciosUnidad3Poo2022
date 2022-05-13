import os
class menu:

    def __init__(self):
      os.system('cls')

    def Menu(self):
     print("Selecciona una opción")
     print("\t1 - primera opción")
     print("\t2 - segunda opción")
     print("\t3 - salir")

    def opcion(self, manejador):
     bandera = True
     while bandera == True:
      self.Menu()
      op = input("inserta un numero valor >> ")
      if op == "1":
       manejador.Codigo()
      elif op == "2":
       manejador.NombreCarrera()
      elif op == "3":
          bandera = False
      else:
       input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")