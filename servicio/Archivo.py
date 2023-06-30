from dominio.Pelicula import Pelicula
class Archivo:

    ruta=r'C:\workspace\python\proyecto1\servicio\Archivo.txt'
    @classmethod
    def crear_pelicula(cls,pelicula:Pelicula):
        with open(Archivo.ruta,'w',encoding='utf8') as archivo:
            archivo.write(f'{pelicula}\n')
            print('ARCHIVO CREADO')

    @classmethod
    def listar_pelicula(cls):
        with open(cls.ruta,'r',encoding='utf8') as archivo:
            for frase in archivo.readlines():
                print(frase)
            print('FINALIZO')
