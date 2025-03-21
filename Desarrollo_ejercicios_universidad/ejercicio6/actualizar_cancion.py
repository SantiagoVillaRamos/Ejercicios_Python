
from interfaz import Opcion, RealizarAccion
from ejecutar_accion import EjecutarAccion
from lista_titulos_canciones import TitulosCanciones
from clases_formularios import TituloCancion, ArtistaCancion, DuracionCancion

class ActualizarCancion(Opcion):
    
    def __init__(self):
        self.__objeto_cancion_actualizada = None
        self.__objeto_nombre_canciones = None
    
    def ejecutar(self, playlist, objeto_validadores):
        validar_texto = objeto_validadores['validar_texto']
        validador_de_numero = objeto_validadores['validador_numero']
        
        titulo_cancion = TituloCancion()
        titulo_cancion.campo_formulario(validar_texto)
        nombre_cancion_validada = titulo_cancion.get_titulo_cancion()
        
        titulos_de_canciones = TitulosCanciones()
        # si en la base de datos existe el titulo que ingreso el usuario, procese a actualizarlo sino, da error.
        if nombre_cancion_validada in titulos_de_canciones.titulos_canciones(playlist):
            
            titulo_nuevo_de_cancion = TituloCancion()
            titulo_nuevo_de_cancion.campo_formulario(validar_texto)
            titulo_cancion_validado = titulo_nuevo_de_cancion.get_titulo_cancion()
                    
            nombre_del_artista = ArtistaCancion()
            nombre_del_artista.campo_formulario(validar_texto)
            nombre_artista_validado = nombre_del_artista.get_nombre_artista()
                    
            duracion_cancion = DuracionCancion()
            duracion_cancion.campo_formulario(validador_de_numero)
            duracion_cancion_validado = duracion_cancion.get_duracion()
            
            self.__objeto_cancion_actualizada = {'titulo_de_cancion': titulo_cancion_validado, 'nombre_artista': nombre_artista_validado,'duracion_cancion': duracion_cancion_validado,}
            self.__objeto_nombre_canciones = {'nombre_cancion_validada': nombre_cancion_validada, 'titulo_nuevo_cancion': titulo_cancion_validado}

            # inyeccion de dependencias para ejecutar la accion de actualizar la cancion en la playlist
            guardar_en_playlist = ActualizarCancionEnPlaylist()
            actualizar_en_playlist = EjecutarAccion(guardar_en_playlist)
            actualizar_en_playlist.ejecutar_accion(playlist, self.get_objeto_cancion_actualizada(), self.get_objeto_nombres_canciones())
        else:
            print(f'\nLa cancion "{nombre_cancion_validada}" no existe en la base de datos')
            print(f'\nLa duracion total de las canciones es: {playlist.duracion_total_de_cancion()} minutos')        

    def get_objeto_cancion_actualizada(self):
        return self.__objeto_cancion_actualizada 
    
    def get_objeto_nombres_canciones(self):
        return self.__objeto_nombre_canciones


class ActualizarCancionEnPlaylist(RealizarAccion):
    
    def realizar_accion(self,  playlist, objeto_cancion, objeto_titulo):
        
        nombre_cancion_validada = objeto_titulo['nombre_cancion_validada']
        titulo_nuevo_cancion = objeto_titulo['titulo_nuevo_cancion']
        
        if playlist.actualizar_cancion(nombre_cancion_validada, objeto_cancion):         
            print(f'\nLa cancion "{nombre_cancion_validada}" se actualizo a "{titulo_nuevo_cancion}" ')
            print(f'\nLa duracion total de las canciones es: {playlist.duracion_total_de_cancion()} minutos')
