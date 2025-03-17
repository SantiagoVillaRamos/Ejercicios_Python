
class TitulosCanciones:
    def titulos_canciones(self, actualizar_cancion_playlist):
        nombres_canciones = [canciones['titulo_de_cancion'] for canciones in actualizar_cancion_playlist.get_canciones()]
        return nombres_canciones