
from interfaz import InterfazOpciones
from agregar_vehiculo_velocidad import AgregarVehiculoYVelocidad
from velocidad_maxima import VelocidadMaxima
from mostrar_vehiculos import MostrarVehiculos
from salir import Salir 

class OpcionesUsuario(InterfazOpciones):
    
    # Mapeo de opciones a clases
    def __init__(self):
        self.opciones_de_usuario = {
            1:AgregarVehiculoYVelocidad(),
            2:VelocidadMaxima(),
            3:MostrarVehiculos(),
            4:Salir()
        }
     
    def realizar_accion(self, opcion, data, objeto):
        
        opcion_usuario = self.opciones_de_usuario.get(opcion)
        
        if opcion_usuario:
            opcion_usuario.ejecutar(data, objeto)
        else:
            print('\n-Opcion no valida')