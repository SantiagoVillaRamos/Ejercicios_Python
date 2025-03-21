
from interfaz import AlmacenamientoCanciones

class AlmacenamientoEnLista(AlmacenamientoCanciones):
    
    def __init__(self):
        self.__canciones = []
    
    def agregar_canciones(self, data):
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
            else:
                False
        return titulo_cancion
    
    def duracion_total_de_cancion(self):
        duracion = self.get_canciones()
        return sum(cancion['duracion_cancion'] for cancion in duracion)
        
    
    def get_canciones(self):
        return self.__canciones
        

# clase negocio que maneja las operaciones de la playlist
# se encarga de agregar, actualizar, eliminar y calcular la duracion total de las canciones
class Playlist:

    def __init__(self, almacenamiento: AlmacenamientoCanciones):
        self.almacenamiento = almacenamiento
        
    def agrear_cancion(self, data):
        return self.almacenamiento.agregar_canciones(data)
        
        
    def actualizar_cancion(self, nombre_cancion, nueva_info):
        return self.almacenamiento.actualizar_cancion(nombre_cancion, nueva_info)
    
    
    def eliminar_cancion(self, data):
        return self.almacenamiento.eliminar_cancion(data)
    
    
    def duracion_total_de_cancion(self):
        return self.almacenamiento.duracion_total_de_cancion()
    
    
    def get_canciones(self):
        return self.almacenamiento.get_canciones()