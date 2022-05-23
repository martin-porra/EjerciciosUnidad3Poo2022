from ManejadorEquipos import  ManejaEquipos
from Clasemenu import  Menu
from  ManejadorContrato import ManejaContratos
from ManejadorJugador import ManejadorJugador
if __name__ == '__main__':
    manejadorequipo = ManejaEquipos()
    manejadorequipo.Cargar()
    manejadorcontrato = ManejaContratos()
    manejadorjugador = ManejadorJugador()
    menu = Menu()
    menu.opcion(manejadorjugador, manejadorequipo, manejadorcontrato)
