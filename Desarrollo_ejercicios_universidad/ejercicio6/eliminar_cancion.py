
from interfaz import Opcion
from clases_formularios import TituloCancion

class EliminarCancion(Opcion):
    
    def __init__(self):
        self.__nombre_cancion = None
    
    def ejecutar(self, playlist, objeto_validadores):
        validar_texto = objeto_validadores['validar_texto']
        
        eliminar_cancion = TituloCancion()
        eliminar_cancion.campo_formulario(validar_texto)
        nombre_cancion = eliminar_cancion.get_titulo_cancion()
        
        self.__nombre_cancion = playlist.eliminar_cancion(nombre_cancion)
        
        imprimir_mensajes = ImprimirMensajes()
        imprimir_mensajes.imprimir_mensajes(playlist, self.get_nombre_cancion(), nombre_cancion) 
    
    def get_nombre_cancion(self):
        return self.__nombre_cancion
        
        
class ImprimirMensajes:
    def imprimir_mensajes(self, playlist, get_nombre_cancion, nombre_cancion):
        
        if get_nombre_cancion != nombre_cancion:
            print(f'\n---La cancion "{nombre_cancion}" ha sido eliminada de la lista')
            print(f'\n-La duracion total de las canciones es: {playlist.duracion_total_de_cancion()} minutos-')
        else:
            print(f'\nLa cancion "{nombre_cancion}"  no se encuentra en la lista---')
            print(f'\nLa duracion total de las canciones es: {playlist.duracion_total_de_cancion()} minutos')
