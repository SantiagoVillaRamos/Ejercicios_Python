from interfaz import RealizarAccion

class EjecutarAccion:
    
    def __init__(self, accion: RealizarAccion):
        self.__accion = accion
        
    def ejecutar_accion(self, accion_objeto_uno, accion_objeto_dos, accion_objeto_tres):
        self.__accion.realizar_accion(accion_objeto_uno, accion_objeto_dos, accion_objeto_tres)
 