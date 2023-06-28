from servicio.Archivo import *
from dominio.Pelicula import *
import os
def run():
    pelicula=Pelicula('Batman','Superheroe',1.20)
    Archivo.crear_pelicula(pelicula)







if __name__=='__main__':
    run()









