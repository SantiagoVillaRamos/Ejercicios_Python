from abc import ABC, abstractmethod

class AlmacenamientoCanciones(ABC):
    
    @abstractmethod
    def agregar_canciones(self, data):
        pass
    
    @abstractmethod
    def actualizar_cancion(self, nombre_cancion, nueva_info):
        pass
    
    @abstractmethod
    def eliminar_cancion(self, data):
        pass
    
    @abstractmethod
    def duracion_total_de_cancion(self):
        pass
    
class AlmacenamientoEnLista(AlmacenamientoCanciones):
    
    def __init__(self):
        self.__canciones = []
    
    def agregar_canciones(self, data):
        self.__canciones.append(data)
        
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
    
    def get_canciones(self):
        return self.__canciones
        

# clase playlist.
class Playlist:

    def __init__(self, almacenamiento: AlmacenamientoCanciones):
        self.almacenamiento = almacenamiento
        
    def agrear_cancion(self, data):
        self.almacenamiento.agregar_canciones(data)
        
        
    def actualizar_cancion(self, nombre_cancion, nueva_info):
        self.almacenamiento.actualizar_cancion(nombre_cancion, nueva_info)
    
    
    def eliminar_cancion(self, data):
        self.almacenamiento.eliminar_cancion(data)
    
    
    def duracion_total_de_cancion(self):
        duracion = self.almacenamiento.get_canciones()
        return sum(cancion['duracion_cancion'] for cancion in duracion)
        