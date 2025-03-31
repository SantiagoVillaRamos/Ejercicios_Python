from interfaz import InterfazEjecutarAccionUsuario, InterfazEjecutarAccion
from clases_formulario import FormularioSalirDelPrograma


class Salir(InterfazEjecutarAccionUsuario):
    
    """Pregunta si quiere continuar en el programa o salir"""
    
    def __init__(self):
        self.lista_opciones = None
        self.respuestas = {
            'si': SalirPrograma(),
            'no': NoSalirPrograma(),
        }
    
    def ejecutar(self, data, objeto):
        
        opcion_usuario = FormularioSalirDelPrograma()
        opcion_usuario.mostrar(objeto)
        
        opcion = opcion_usuario.get_obtener_datos()
        
        if opcion in self.respuestas:
            self.respuestas[opcion].ejecutar_accion_usuario(data)
        else:
            print('\n-Respuesta no valida')
        
  
        
class SalirPrograma(InterfazEjecutarAccion):
    
    def ejecutar_accion_usuario(self, data):
        data.get_marca()
        print('\n-Programa finalizado')
        exit()


class NoSalirPrograma(InterfazEjecutarAccion):
    
    def ejecutar_accion_usuario(self, data):
        print('\n-Programa no finalizado')