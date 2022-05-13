from claseManejador import  manejadorFacultad
from ClaseMenu import  menu
if __name__ == '__main__':

     unmanejador = manejadorFacultad()
     unmanejador.leerArchivo()
     Menu = menu()
     Menu.opcion(unmanejador)