
from interfaz import Actualizar
from logica import LogicaActualizarCancion
from lista_titulos_canciones import TitulosCanciones
from clases_formularios import TituloCancion, ArtistaCancion, DuracionCancion

class ActualizarCancion(Actualizar):
    def actualizar_cancion(self, data):
        
        actualizar_cancion_playlist = data['playlist']
        validar_texto = data['validar_texto']
        validador_de_numero = data['validador_numero']
        
        titulo_cancion = TituloCancion()
        titulo_cancion.campo_formulario(validar_texto)
        nombre_cancion_validada = titulo_cancion.get_titulo_cancion()
        
        titulos_de_canciones = TitulosCanciones()
        
        # si en la base de datos existe el titulo que ingreso el usuario, procese a actualizarlo
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
            
            objeto = {
                'titulo_nuevo_cancion': titulo_nuevo_cancion,
                'nombre_nuevo_artista': nombre_nuevo_artista,
                'numero_nuevo_validado': numero_nuevo_validado,
                'nombre_cancion_validada': nombre_cancion_validada
            }
            
            actualizar = CrearObjetoCancionActualizada()
            actualizar.crear_objeto_cancion_actualizada(objeto, actualizar_cancion_playlist)

        else:
            print(f'\nLa cancion "{nombre_cancion_validada}" no existe en la base de datos')
            print(f'\nLa duracion total de las canciones es: {actualizar_cancion_playlist.duracion_total_de_cancion()} minutos')        


class CrearObjetoCancionActualizada:
    def crear_objeto_cancion_actualizada(self, data, actualizar_cancion_playlist):
        
        titulo_nuevo_cancion = data['titulo_nuevo_cancion']
        nombre_nuevo_artista = data['nombre_nuevo_artista']
        numero_nuevo_validado =data['numero_nuevo_validado']
        nombre_cancion_validada = data['nombre_cancion_validada']
        
        cancion_actualizada = {'titulo_de_cancion': titulo_nuevo_cancion, 'artista_cancion': nombre_nuevo_artista,'duracion_cancion': numero_nuevo_validado}
        objeto = {
            'titulo_nuevo_cancion': titulo_nuevo_cancion,
            'nombre_cancion_validada': nombre_cancion_validada
        }
        logica_actualizar_cancion = LogicaActualizarCancion()
        logica_actualizar_cancion.actualizar_cancion(actualizar_cancion_playlist, cancion_actualizada, objeto)