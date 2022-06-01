import os
from ManejadorContrato import  ManejaContratos
from ManejadorJugador import  ManejadorJugador
from ManejadorEquipos import  ManejaEquipos
from ClaseJugador import Jugador
class Menu:

    def __init__(self):
      os.system('cls')

    def Menu(self):
     print("Selecciona una opción")
     print("\t1 - Crear Jugador")
     print("\t2 - Crear contrato")
     print("\t3 - Consultar jugador contratado por dni")
     print("\t4 - Ingresar identificador equipo")
     print("\t5 - Importe por equipo ")
     print("\t5 - Guardar contrato ")

    def opcion(self,manejadorjugador,manejadorequipo,manejadorcontrato,encoder):
     bandera = True
     while bandera == True:
      self.Menu()
      op = input("inserta un numero valor >> ")
      if op == "1":
       #manejadorjugador.crearjugador()
       jugador = Jugador('martin',43156808,'San Juan','Argentina','2000/12/02')
       manejadorjugador.agregarJugador(jugador)
      elif op == "2":
       print('Elija un jugador y equipo para generar un contrato')
       manejadorjugador.listar()
       print('--------------------')
       print(manejadorequipo)
       jugador = int(input('ingresar indice de jugador '))
       equipo = int(input('ingresar indice de equipo '))
       manejadorcontrato.CrearContrato(manejadorjugador.getlista()[jugador],manejadorequipo.getlista()[equipo])
      elif op == "3":
          manejadorcontrato.ConsultarDni()
      elif op == "4":
          print(manejadorequipo)
          manejadorcontrato.identificadorequipo()
      elif op == "5":
          manejadorcontrato.identificarnombre()
      elif op == "6":
          listaJSON = manejadorcontrato.guardarJSON()
          encoder.guardarJSONArchivo(listaJSON, 'Contratos.json')
          print('Archivo guardado')
      else:
       input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")