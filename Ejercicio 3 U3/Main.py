from ManejadorEquipos import  ManejaEquipos
from Clasemenu import  Menu
from  ManejadorContrato import ManejaContratos
from ManejadorJugador import ManejadorJugador
from Objetencoder import  ObjectEncoder
if __name__ == '__main__':
    encoder = ObjectEncoder()
    manejadorequipo = ManejaEquipos()
    manejadorequipo.Cargar()
    manejadorcontrato = ManejaContratos()
    manejadorjugador = ManejadorJugador()
    menu = Menu()
    menu.opcion(manejadorjugador, manejadorequipo, manejadorcontrato,encoder)
