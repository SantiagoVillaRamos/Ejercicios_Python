from abc import ABC, abstractmethod

# interfaz crear
class Crear(ABC):
    @abstractmethod
    def crear_cancion(self, data):
        pass
    
# interfaz eliminar
class Eliminar(ABC):
    @abstractmethod
    def eliminar_cancion(self, data):
        pass

# interfaz actualizar
class Actualizar(ABC):
    @abstractmethod
    def actualizar_cancion(self, data):
        pass
    
# interfaz campo formulario
class CampoFormulario(ABC):
    @abstractmethod
    def campo_formulario(self, data):
        pass