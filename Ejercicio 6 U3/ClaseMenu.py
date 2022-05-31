import os
from Manejador import  Manejador
from ClaseLavaropa import Lavaropa
from ClaseObjetencoder import  ObjectEncoder
class Menu:

    def __init__(self):
      os.system('cls')

    def Menu(self):
     print("Selecciona una opción")
     print("\t1 - Insertar un aparato en la colección en una posición determinada")
     print("\t2 - Agregar un aparato a la colección ")
     print("\t3 - Mostrar por pantalla qué tipo de objeto se encuentra almacenado en dicha posición")
     print("\t4 - Mostrar la cantidad de heladeras, lavarropas y televisores cuya marca sea phillips")
     print("\t5 - Mostrar la marca de todos los lavarropas que tienen carga superior")
     print("\t6 - Mostrar para todos los aparatos que la empresa tiene a la venta, marca, país de fabricación e importe de venta.")
     print("\t7 - Almacenar los objetos de la colección Lista en el archivo")
     print("\t8 - salir")

    def opcion(self, manejador,encoder):
     bandera = True
     while bandera == True:
      self.Menu()
      op = input("inserta un numero valor >> ")
      if op == "1":
       pos = int(input('Ingresar posicion donde insertara el elemento '))
       aparato = manejador.crearaparato()
       manejador.insertarElemento(aparato,pos)
      elif op == "2":
       aparato = manejador.crearaparato()
       manejador.agregarElemento(aparato)
      elif op == "3":
          posicion = int(input('Ingresar posicion '))
          manejador.mostrarElemento(posicion)
      elif op == "4":
          manejador.Aparatosphillips()
      elif op == "5":
        manejador.marcalavaropas()
      elif op == "6":
          manejador.mostrarDatos()
      elif op == "7":
          listaJSON = manejador.guardarJSON()
          encoder.guardarJSONArchivo(listaJSON, 'Aparato.json')
          print('Archivo guardado')
      elif op == "8":
          bandera = False
      else:
       input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")