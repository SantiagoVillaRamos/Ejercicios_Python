
from interfaz import InterfazOpciones
from agregar_puntos import AgregarPuntos
from restar_puntos import RestarPuntosJuego
from consultar_puntuacion import ConsultarPuntuacion
from salir import Salir 

class OpcionesUsuario(InterfazOpciones):
    
    # Mapeo de opciones a clases
    def __init__(self):
        self.opciones_de_usuario = {
            1:AgregarPuntos(),
            2:RestarPuntosJuego(),
            3:ConsultarPuntuacion(),
            4:Salir()
        }
     
    def realizar_accion(self, opcion, data, objeto):
        
        opcion_usuario = self.opciones_de_usuario.get(opcion)
        
        if opcion_usuario:
            opcion_usuario.ejecutar(data, objeto)
        else:
            print('\n-Opcion no valida')