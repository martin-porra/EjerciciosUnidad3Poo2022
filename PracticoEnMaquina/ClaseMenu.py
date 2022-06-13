import os
class menu:

    def __init__(self):
      os.system('cls')

    def Menu(self):
     print("Selecciona una opción")
     print("\t1 - primera opción")
     print("\t2 - segunda opción")
     print("\t3 - tercera opcion")
     print("\t4 - cuarta opcion")
     print("\t5 - salir")

    def opcion(self, manejador1,manejador2):
     bandera = True
     while bandera == True:
      self.Menu()
      op = input("inserta un numero valor >> ")
      if op == "1":
       manejador1.PedidosPendientes()
      elif op == "2":
       manejador2.PedidoEntregado(manejador1)
      elif op == "3":
          manejador2.iguales()
      elif op == "4":
          manejador2.ordenar()
      elif op == "5":
          bandera = False
      else:
       input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")