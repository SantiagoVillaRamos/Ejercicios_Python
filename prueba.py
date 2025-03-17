#### 5. **D - Principio de Inversión de Dependencias (Dependency Inversion Principle - DIP)**

# Este principio establece que los módulos de alto nivel no deben depender de módulos de bajo nivel. Ambos deben depender de abstracciones. Además, las abstracciones no deben depender de los detalles. Los detalles deben depender de las abstracciones.

# - **Ejemplo:** Si tienes una clase `NotificacionService` que depende directamente de una clase `EmailService`, estás acoplando el servicio de notificaciones a un tipo específico de notificación. En su lugar, podrías tener una interfaz `IMessageService` que `EmailService` implemente, y `NotificacionService` dependa de `IMessageService`. Esto te permitiría cambiar fácilmente el tipo de servicio de mensajes en el futuro.

from abc import ABC, abstractmethod

class IMessageService(ABC):
    @abstractmethod
    def notificacion(self, message):
        pass

class EmailService:
    pass

class NotificacionService(IMessageService):
    def notificacion(self, message):
        # logica que maneja el envio de mensajes
        pass
    
# ### . **L - Principio de Sustitución de Liskov (Liskov Substitution Principle - LSP)**

# Este principio establece que los objetos de una superclase deben ser reemplazables por objetos de una subclase sin afectar la corrección del programa.

# - **Ejemplo:** Si tienes una clase `Pájaro` y una subclase `Pingüino`, no deberías asumir que todos los pájaros pueden volar. Si `Pájaro` tiene un método `volar`, `Pingüino` no debería heredar ese método, ya que los pingüinos no vuelan. En su lugar, podrías tener una interfaz `Volador` que solo las clases que pueden volar implementen.

class Volar(ABC):
    @abstractmethod
    def volar(self):
        pass

class Pajaro:
    pass
    
class Pinguino(Pajaro):
    pass

class Aguila(Pajaro,Volar):
    def volar(self):
        return super().volar()