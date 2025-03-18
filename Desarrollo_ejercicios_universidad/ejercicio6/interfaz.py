from abc import ABC, abstractmethod
    
# interfaz campo formulario
class CampoFormulario(ABC):
    @abstractmethod
    def campo_formulario(self, data):
        pass
    
class Opcion(ABC):
    @abstractmethod
    def ejecutar(self, playlist, objeto):
        pass
    
    
class EjecutarOpcion(ABC):
    @abstractmethod
    def ejecutar_opcion(self, data):
        pass