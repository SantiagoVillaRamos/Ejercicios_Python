from crear_cancion import CrearCancion
from actualizar_cancion import ActualizarCancion
from eliminar_cancion import EliminarCancion
from mostrar_duracion_total import MostrarDuracionTotal

# clase principal que maneja las opciones del usuario
class OpcionUsuario:
    # Mapeo de opciones a clases
    def __init__(self):
        self.opciones = {
            1:CrearCancion(),
            2:EliminarCancion(),
            3:ActualizarCancion(),
            4:MostrarDuracionTotal(),
        }
    
    def opciones_usuario(self, opcion_usuario, playlist, objeto):
        
        opcion = self.opciones.get(opcion_usuario)
        
        if opcion:
            opcion.ejecutar(playlist, objeto)
        else:
            print('\n-Opcion no valida')
            