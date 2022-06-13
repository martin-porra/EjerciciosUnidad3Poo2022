from ManejadorRepartidor import  ManejadorRepartidores
from  ManejadorPedido import  ManejadorPedidos
from ClaseMenu import  menu
if __name__ == '__main__':
 manejadorRepartidores = ManejadorRepartidores()
 manejadorpedidos = ManejadorPedidos()
 manejadorpedidos.Cargar()
 Menu = menu()
 Menu.opcion(manejadorpedidos,manejadorRepartidores)


