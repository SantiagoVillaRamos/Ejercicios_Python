from abc import ABC, abstractmethod

class InterfazEmpleado(ABC):
    @abstractmethod
    def agregar_datos_persona(self, datos):
        pass
    
    @abstractmethod
    def set_nombre_nuevo(self, nombre_persona, nuevo_nombre):
        pass
    
    @abstractmethod
    def aumentar_salario(self, nombre_persona, aumento):
        pass
    
    @abstractmethod
    def set_nuevo_salario(self, nombre_persona, nuevo_salario):
        pass
 

# interfaz opciones usuario
class InterfazOpciones(ABC):
    @abstractmethod
    def realizar_accion(self, opcion, data, objeto):
        pass
       
    
class InterfazValidadores(ABC):
    @abstractmethod
    def validar(self, data):
        pass
    
    @abstractmethod
    def obtener_datos(self):
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
    