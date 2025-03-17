
from interfaz import Eliminar
from logica import LogicaEliminarCancion

class EliminarCancion(Eliminar): 
    def eliminar_cancion(self, data):
        
        eliminar_cancion_playlist = data
        titulo_de_cancion = input('\nIngresa el titulo de la cancion a eliminar: ')
        titulo_cancion = eliminar_cancion_playlist.eliminar_cancion(titulo_de_cancion)
        
        logica_eliminar_cancion = LogicaEliminarCancion()
        logica_eliminar_cancion.eliminar_cancion(eliminar_cancion_playlist, titulo_cancion, titulo_de_cancion)
 