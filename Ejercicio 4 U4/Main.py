from  ManejadorCalefactores import  ManejaCalefactor
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
    manejador.mostrar()
