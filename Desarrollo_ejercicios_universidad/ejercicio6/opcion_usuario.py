from createDeleteUpdate import EliminarCancion, CrearCancionEnPlaylist, ActualizarCancion

class OpcionUsuario:
    def opciones_usuario(self, opcion_usuario, playlist, objeto):
        
        if opcion_usuario == 1:  
            crear_cancion = CrearCancionEnPlaylist()
            crear_cancion.crear_cancion(objeto)

        elif opcion_usuario == 2:
            eliminar_cancion = EliminarCancion()
            eliminar_cancion.eliminar_cancion(playlist)
            
        elif opcion_usuario == 3:
            actualizar_cancion = ActualizarCancion()
            actualizar_cancion.actualizar_cancion(objeto)
            
        elif opcion_usuario == 4:
            print(f'\nLa duracion total de las canciones es: {playlist.duracion_total_de_cancion()} minutos')
            
        return opcion_usuario