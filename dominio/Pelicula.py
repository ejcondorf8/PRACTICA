class Pelicula:
    contador=0
    @classmethod
    def _aumentar_id(cls):
        cls.contador+=1
        return cls.contador
        
    def __init__(self,nombre:str,categoria:str,precio:float) -> None:
        self._id=Pelicula._aumentar_id()
        self._nombre=nombre
        self._categoria=categoria
        self._precio=precio

    def __str__(self) -> str:
        return f'ID DE LA PELICULA {self._id} NOMBRE DE LA PELICULA {self._nombre} Y PRECIO DE LA PELICULA {self._precio} '
    




