
class LogicaCrearCancion:
    def crear_cancion(self, crear_cancion_playlist, cancion, titulo_de_cancion):
        
        if crear_cancion_playlist.agrear_cancion(cancion):
            print(f'\nLa Cancion "{titulo_de_cancion}" se guardo')
        else:
            print(f'\nNo se guardo')
        
        print(f'\nLa duracion total de las canciones es: {crear_cancion_playlist.duracion_total_de_cancion()} minutos')
        
        
class LogicaEliminarCancion:
    def eliminar_cancion(self, eliminar_cancion_playlist, titulo_cancion, titulo_de_cancion):
        
        if titulo_cancion != titulo_de_cancion:
            print(f'\n---La cancion "{titulo_de_cancion}" ha sido eliminada de la lista')
            print(f'\n-La duracion total de las canciones es: {eliminar_cancion_playlist.duracion_total_de_cancion()} minutos-')
        else:
            print(f'\nLa cancion "{titulo_de_cancion}"  no se encuentra en la lista---')
            print(f'\nLa duracion total de las canciones es: {eliminar_cancion_playlist.duracion_total_de_cancion()} minutos')
            
            
class LogicaActualizarCancion:
    def actualizar_cancion(self, actualizar_cancion_playlist, cancion_actualizada, objeto):
        
        nombre_cancion_validada = objeto['nombre_cancion_validada']
        titulo_nuevo_cancion = objeto['titulo_nuevo_cancion']
        
        if actualizar_cancion_playlist.actualizar_cancion(nombre_cancion_validada, cancion_actualizada):         
            print(f'\nLa cancion "{nombre_cancion_validada}" se actualizo a "{titulo_nuevo_cancion}" ')
            print(f'\nLa duracion total de las canciones es: {actualizar_cancion_playlist.duracion_total_de_cancion()} minutos')