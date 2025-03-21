from abc import ABC, abstractmethod
    
# interfaz campo formulario
class CampoFormulario(ABC):
    @abstractmethod
    def campo_formulario(self, data):
        pass
    
class Opcion(ABC):
    @abstractmethod
    def ejecutar(self, playlist, objeto_validadores):
        pass
    
    
class EjecutarOpcion(ABC):
    @abstractmethod
    def ejecutar_opcion(self, playlist):
        pass
    
    
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
    
    
class OpcinesUsuario(ABC):
    
    @abstractmethod
    def opciones_usuario(self, opcion_usuario, playlist, objeto_validadores):
        pass
    

class RealizarAccion(ABC):
    
    @abstractmethod
    def realizar_accion(self, playlist, objeto_cancion, objeto_titulo):
        pass