
from clases_formulario import FormularioVelocidad, FormularioVehiculo
from interfaz import InterfazEjecutarAccion


class Formulario(InterfazEjecutarAccion):
    
    def __init__(self):
        self.__lista_opciones = None
        self.respuestas = {
            'nombre': FormularioVehiculo(),
            'velocidad': FormularioVelocidad()
        }
        self.__datos = {}
        
    def lista_opiones(self, lista_opciones):
        self.__lista_opciones = lista_opciones
        
        
    def ejecutar_accion_usuario(self, data):
        # Verificar si la clave de respuesta está en la lista de valores
        for valor in self.__lista_opciones:
            if valor in self.respuestas:
                self.respuestas[valor].mostrar(data)
                self.__datos[valor] = self.respuestas[valor].get_obtener_datos()
            else:
                print('\n-Opción no válida')

    def get_datos(self):
        return self.__datos 
    