from  ClaseObjetencoder import  ObjectEncoder
from Manejador import Manejador
from ClaseMenu import Menu
if __name__ == "__main__":
    jsonF = ObjectEncoder()
    Aparatos = Manejador()
    diccionario = jsonF.leerJSONArchivo('aparatoselectronicos.json')
    Aparatos = jsonF.decodificarDiccionario(diccionario)
    menu = Menu()
    menu.opcion(Aparatos,jsonF)