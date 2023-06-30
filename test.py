from servicio.Archivo import *
from dominio.Pelicula import *
import os

def devolver_pelicula(nombre,categoria,precio):
    return Pelicula(nombre,categoria,precio)
def run():
    while True:
        print(f'''
              1.Añadir Pelicula
              2.Listar Pelicula
              3.Borar archivo
              4.Salio
                     ''')
        try:
            opcion=int(input('DIGITE UNA OPCION'))
        except Exception as e :
            print('OCURRIO UN ERRO')

        if opcion == 4 :
            print('HASTA LA PROXIMA')
            break
        elif opcion == 1:
            nombre=input('DAME NOMBRE DE LA PELICULA: ')
            categoria=input('DAME LA CATERGORIA: ')
            precio=float(input('DAME PRECIO: '))
            pelicula = devolver_pelicula(nombre,categoria,precio)
            Archivo.crear_pelicula(pelicula)
        elif opcion == 2:
            Archivo.listar_pelicula()
                
        









if __name__=='__main__':
    run()









