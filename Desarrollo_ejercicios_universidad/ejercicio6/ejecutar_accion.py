from interfaz import RealizarAccion

class EjecutarAccion:
    
    def __init__(self, accion: RealizarAccion):
        self.__accion = accion
        
    def ejecutar_accion(self, playlist, objeto_cancion, objeto_titulo):
        self.__accion.realizar_accion(playlist, objeto_cancion, objeto_titulo)
