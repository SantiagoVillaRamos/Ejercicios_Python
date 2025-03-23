from interfaz import RealizarAccion, RealizarAccionOpcion

class EjecutarAccion:
    
    def __init__(self, accion: RealizarAccion):
        self.__accion = accion
        
    def ejecutar_accion(self, accion_objeto_uno, accion_objeto_dos, accion_objeto_tres):
        self.__accion.realizar_accion(accion_objeto_uno, accion_objeto_dos, accion_objeto_tres)
 
 
 
class RealizarAccionOpcionPrograma:
    
    def __init__(self, accion: RealizarAccionOpcion):
        self.__accion = accion
    
    def realizar_accion(self, accion):
        self.__accion.preguntar(accion)
        
    def get_datos(self):
        return self.__accion.get_datos()
        
