from ManejadorFlores import ManejadorFlores
from  ManejadoresRamos import ManejadorRamos
from  ClaseMenu import Menu
if __name__ == '__main__':
    manejadorFlores= ManejadorFlores()
    manejadorFlores.Cargar()
    manejaRamos = ManejadorRamos()
    menu = Menu()
    menu.opcion(manejaRamos,manejadorFlores)