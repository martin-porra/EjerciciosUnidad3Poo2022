from clasemanejador import  manejador
from claseobject import ObjectEncoder
from menu import Menu
from ClaseTesorero import ITesorero
from ClaseDirector import IDirector


def tesorero(manejador: ITesorero):
  bandera = True
  while bandera:
   cuil = input('Ingrese el cuil de un agente (N para salir): ')
   if cuil.lower() == 'n':
    bandera = False
   else:
    manejador.gastosSueldoPorEmpleado(cuil)

def director(manejador: IDirector):
    bandera = True
    while  bandera:
        print('1- Modificar el sueldo basico de un empleado')
        print('2- Modificar el importe extra de un Docente Investigador')
        print('3- Modificar el porcentaje por cargo')
        print('4- Modificar el porcentaje por categoria')
        print('5- Salir')
        opcion = int(input('Ingrese una opcion: '))
        if opcion == 1:
            cuil = input('Ingrese el cuil de un agente: ')
            basico = float(input('Ingrese el nuevo sueldo basico: '))
            manejador.modificarBasico(cuil, basico)
        elif opcion == 2:
            cuil = input('Ingrese el cuil de un docente investigador: ')
            ImporteExtra = float(input('Ingrese el nuevo importe extra: '))
            manejador.modificarImporteExtra(cuil, ImporteExtra)
        elif opcion == 3:
            porcentajecargo = float(input('Ingrese el nuevo porcentaje: '))
            manejador.modificarPorcentajeporcargo(porcentajecargo)
        elif opcion == 4:
            porcentajecate = float(input('Ingrese el nuevo porcentaje: '))
            manejador.modificarPorcentajeporcategoría(porcentajecate)
        elif opcion == 5:
            bandera = False
        else:
            print('ERROR: Opcion ingresda incorrecta!')



if __name__ == '__main__':
 maneja = manejador()
 encoder = ObjectEncoder()
 lista = encoder.leerJSONArchivo('personal.json')
 maneja.llenar(lista)
 men = Menu()
 bandera1 = True
 while bandera1:
  print('1 --- Menu de usuario\n2 --- Menu de gestion\n3 --- Salir ')
  op = input('Ingresar opcion ')
  if op == '1':
   bandera = True
   while bandera:
    usuario= input('Ingresar usuario ')
    contraseña = input('Ingresar Contraseña ')
    if usuario == 'uTesoreso' and contraseña == 'ag@74ck':
     tesorero(ITesorero(maneja))
     bandera = False
    elif usuario == 'uDirector' and contraseña == 'ufC77#!1':
     director(IDirector(maneja))
     bandera = False
    else:
     print('Contraseña y/o Usuario incorrecotos')
  elif op == '2':
    men.Opcion(maneja,encoder)
  elif op == '3':
   bandera1 = False
   print('Cerrando....')
  else:
   print('Opcion incorrecta, vuelva a ingresar')



