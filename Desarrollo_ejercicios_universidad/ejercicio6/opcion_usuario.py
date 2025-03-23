from actualizar_cancion import ActualizarCancion
from eliminar_cancion import EliminarCancion
from mostrar_duracion_total import SalirDelPrograma
from interfaz import RealizarAccion
from crear_cancion_refac import CrearCancion

# clase principal que maneja las opciones del usuario
class OpcionUsuario(RealizarAccion):
    # Mapeo de opciones a clases
    def __init__(self):
        self.opciones_de_usuario = {
            1:CrearCancion(),
            2:EliminarCancion(),
            3:ActualizarCancion(),
            4:SalirDelPrograma(),
        }
    
    def realizar_accion(self, accion_objeto_uno, accion_objeto_dos, accion_objeto_tres):
        
        opcion = self.opciones_de_usuario.get(accion_objeto_uno)
        
        if opcion:
            opcion.ejecutar(accion_objeto_dos, accion_objeto_tres)
        else:
            print('\n-Opcion no valida')