from abc import ABC, abstractmethod

# Interfaz Banco
# Define los métodos que deben implementar las clases que interactúan con el banco
class InterfazBanco(ABC):
    @abstractmethod
    def depositar(self, cantidad):
        pass
    
    @abstractmethod
    def retirar(self, cantidad):
        pass
 
    
# interfaz formulario
class InterfazFormulario(ABC):
    @abstractmethod
    def mostrar(self, data):
        pass
    
    @abstractmethod
    def get_obtener_datos(self):
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
    

# interaz validadores
class InterfazValidadores(ABC):
    @abstractmethod
    def validar(self, data):
        pass
    
    @abstractmethod
    def obtener_datos(self):
        pass