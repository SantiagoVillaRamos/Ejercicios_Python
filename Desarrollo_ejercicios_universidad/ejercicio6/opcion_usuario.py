from crear_cancion import CrearCancion
from actualizar_cancion import ActualizarCancion
from eliminar_cancion import EliminarCancion
from mostrar_duracion_total import SalirDelPrograma

# clase principal que maneja las opciones del usuario
class OpcionesUsuario:
    # Mapeo de opciones a clases
    def __init__(self):
        self.opciones_de_usuario = {
            1:CrearCancion(),
            2:EliminarCancion(),
            3:ActualizarCancion(),
            4:SalirDelPrograma(),
        }
    
    def opciones_usuario(self, opcion_usuario, playlist, objeto_validadores):
        
        opcion = self.opciones_de_usuario.get(opcion_usuario)
        
        if opcion:
            opcion.ejecutar(playlist, objeto_validadores)
        else:
            print('\n-Opcion no valida')
            