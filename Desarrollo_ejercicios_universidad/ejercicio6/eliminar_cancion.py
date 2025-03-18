
from interfaz import Opcion
from clases_formularios import TituloCancion

class EliminarCancion(Opcion):
    
    def __init__(self):
        self.__nombre_cancion = None
    
    def ejecutar(self, playlist, objeto):
        validar_texto = objeto['validar_texto']
        
        eliminar_cancion = TituloCancion()
        eliminar_cancion.campo_formulario(validar_texto)
        nombre_cancion = eliminar_cancion.get_titulo_cancion()
        
        self.__nombre_cancion = playlist.eliminar_cancion(nombre_cancion)
        
        logica_eliminar_cancion = LogicaEliminarCancion()
        logica_eliminar_cancion.eliminar_cancion(playlist, self.get_nombre_cancion(), nombre_cancion) 
    
    def get_nombre_cancion(self):
        return self.__nombre_cancion
        
        
class LogicaEliminarCancion:
    def eliminar_cancion(self, eliminar_cancion_playlist, titulo_cancion, titulo_de_cancion):
        
        if titulo_cancion != titulo_de_cancion:
            print(f'\n---La cancion "{titulo_de_cancion}" ha sido eliminada de la lista')
            print(f'\n-La duracion total de las canciones es: {eliminar_cancion_playlist.duracion_total_de_cancion()} minutos-')
        else:
            print(f'\nLa cancion "{titulo_de_cancion}"  no se encuentra en la lista---')
            print(f'\nLa duracion total de las canciones es: {eliminar_cancion_playlist.duracion_total_de_cancion()} minutos')
