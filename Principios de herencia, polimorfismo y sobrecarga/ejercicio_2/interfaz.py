from abc import ABC, abstractmethod

class InterfazProducto(ABC):
    @abstractmethod
    def get_precio(self):
        pass
    
    @abstractmethod
    def set_precio(self,producto, nuevo_precio):
        pass
    
    @abstractmethod
    def aplicar_descuento(self, objeto):
        pass
    
    
class InterfazValidadores(ABC):
    @abstractmethod
    def validar(self, data):
        pass
    
    @abstractmethod
    def obtener_datos(self):
        pass
    
    
# interfaz opciones usuario
class InterfazOpciones(ABC):
    @abstractmethod
    def realizar_accion(self, opcion, data, objeto):
        pass
    

# interfaz ejecutar accion usuario
class InterfazEjecutarAccionUsuario(ABC):
    @abstractmethod
    def ejecutar(self, data, objeto):
        pass
    

# interfaz ejecutar accion usuario
class InterfazEjecutarAccion(ABC):
    @abstractmethod
    def ejecutar_accion_usuario(self, data): 
        pass
    
    
# interfaz formulario
class InterfazFormulario(ABC):
    @abstractmethod
    def mostrar(self, data):
        pass
    
    @abstractmethod
    def get_obtener_datos(self):
        pass
    