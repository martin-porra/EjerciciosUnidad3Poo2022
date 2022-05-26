from  ClaseObjetencoder import  ObjectEncoder
from Manejador import Manejador
if __name__ == "__main__":
    jsonF = ObjectEncoder()
    Aparatos = Manejador()
    diccionario = jsonF.leerJSONArchivo('Aparato.json')
    Aparatos = jsonF.decodificarDiccionario(diccionario)
