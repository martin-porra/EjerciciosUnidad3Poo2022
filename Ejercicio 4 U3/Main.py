from  ManejadorCalefactores import  ManejaCalefactor
from Menu import Menu
if __name__ == '__main__':
    bandera = True
    while bandera == True:
        try:
            cantidad = int(input('Igresar numero de componentes del arreglo '))
            bandera = False
        except:
            print('debe ser un numero entero')
    manejador = ManejaCalefactor(cantidad)
    manejador.cargar()
    menu = Menu()
    menu.opcion(manejador)
