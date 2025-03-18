
from interfaz import Actualizar
from logica import LogicaActualizarCancion
from lista_titulos_canciones import TitulosCanciones
from clases_formularios import TituloCancion, ArtistaCancion, DuracionCancion

class ActualizarCancion(Actualizar):
    
    def __init__(self):
        self.__objeto = None
        self.__objeto_nombre_canciones = None
    
    def actualizar_cancion(self, data):
        
        actualizar_cancion_playlist = data['playlist']
        validar_texto = data['validar_texto']
        validador_de_numero = data['validador_numero']
        
        titulo_cancion = TituloCancion()
        titulo_cancion.campo_formulario(validar_texto)
        nombre_cancion_validada = titulo_cancion.get_titulo_cancion()
        
        titulos_de_canciones = TitulosCanciones()
        # si en la base de datos existe el titulo que ingreso el usuario, procese a actualizarlo sino, da error.
        if nombre_cancion_validada in titulos_de_canciones.titulos_canciones(actualizar_cancion_playlist):
            
            titulo_nuevo_de_cancion = TituloCancion()
            titulo_nuevo_de_cancion.campo_formulario(validar_texto)
            titulo_nuevo_cancion = titulo_nuevo_de_cancion.get_titulo_cancion()
                    
            nombre_del_artista = ArtistaCancion()
            nombre_del_artista.campo_formulario(validar_texto)
            nombre_nuevo_artista = nombre_del_artista.get_nombre_artista()
                    
            duracion_cancion = DuracionCancion()
            duracion_cancion.campo_formulario(validador_de_numero)
            numero_nuevo_validado = duracion_cancion.get_duracion()
            
            self.__objeto = {'titulo_de_cancion': titulo_nuevo_cancion, 'nombre_artista': nombre_nuevo_artista,'duracion_cancion': numero_nuevo_validado,}
            self.__objeto_nombre_canciones = {'nombre_cancion_validada': nombre_cancion_validada, 'titulo_nuevo_cancion': titulo_nuevo_cancion}

            logica_actualizar_cancion = LogicaActualizarCancion()
            logica_actualizar_cancion.actualizar_cancion(actualizar_cancion_playlist, self.get_objeto_cancion_actualizada(), self.get_objeto_nombre_canciones())
        else:
            print(f'\nLa cancion "{nombre_cancion_validada}" no existe en la base de datos')
            print(f'\nLa duracion total de las canciones es: {actualizar_cancion_playlist.duracion_total_de_cancion()} minutos')        


    def get_objeto_cancion_actualizada(self):
        return self.__objeto 
    
    def get_objeto_nombre_canciones(self):
        return self.__objeto_nombre_canciones
        