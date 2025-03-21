
from interfaz import Opcion, RealizarAccion
from ejecutar_accion import EjecutarAccion
from clases_formularios import TituloCancion

class EliminarCancion(Opcion):
    
    def ejecutar(self, playlist, objeto_validadores):
        validar_texto = objeto_validadores['validar_texto']
        
        eliminar_cancion = TituloCancion()
        eliminar_cancion.campo_formulario(validar_texto)
        nombre_cancion = eliminar_cancion.get_titulo_cancion()
        
        eliminar_cancion_de_playlist = EliminarCancionEnPlaylist()
        eliminar_cancion_de_playlist.eliminar_cancion_de_playlist(playlist, nombre_cancion)
        
        
class EliminarCancionEnPlaylist:
    
    def __init__(self):
        self.__nombre_cancion = None
        
    def eliminar_cancion_de_playlist(self, playlist, nombre_cancion):
        self.__nombre_cancion = playlist.eliminar_cancion(nombre_cancion) 

        # inyeccion de dependencias para ejecutar la accion de eliminar la cancion en la playlist   
        imprimir_mensajes = ImprimirMensajeEliminarCancionEnPlaylist()
        accion_eleminar_cancion = EjecutarAccion(imprimir_mensajes)
        accion_eleminar_cancion.ejecutar_accion(playlist, self.get_nombre_cancion(), nombre_cancion) 
    
    def get_nombre_cancion(self):
        return self.__nombre_cancion


class ImprimirMensajeEliminarCancionEnPlaylist(RealizarAccion):
    
    def realizar_accion(self, accion_objeto_uno, accion_objeto_dos, accion_objeto_tres):
        
        if accion_objeto_dos != accion_objeto_tres:
            print(f'\n---La cancion "{accion_objeto_tres}" ha sido eliminada de la lista')
            print(f'\n-La duracion total de las canciones es: {accion_objeto_uno.duracion_total_de_cancion()} minutos-')
        else:
            print(f'\nLa cancion "{accion_objeto_tres}"  no se encuentra en la lista---')
            print(f'\nLa duracion total de las canciones es: {accion_objeto_uno.duracion_total_de_cancion()} minutos')
