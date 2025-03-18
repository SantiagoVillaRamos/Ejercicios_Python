# clase playlist.
class Playlist:
    
    def __init__(self):
        self.__canciones = []
    
    
    def agrear_cancion(self, data):
        self.__canciones.append(data)
        return True
        

    def actualizar_cancion(self, nombre_cancion, nueva_info):
        for cancion in self.__canciones:
            if cancion['titulo_de_cancion'] == nombre_cancion:
                cancion.update(nueva_info)
                return True
        return nombre_cancion
    
    
    def eliminar_cancion(self, data):
        titulo_cancion = data
        for cancion in self.__canciones:
            if cancion['titulo_de_cancion'] == titulo_cancion:
                self.get_canciones().remove(cancion)
                return True
        return titulo_cancion
    
    
    def duracion_total_de_cancion(self):
        duracion = 0
        for cancion in self.__canciones:
            duracion += cancion['duracion_cancion']
        return duracion

    # lista de canciones creadas
    def get_canciones(self):
        return self.__canciones