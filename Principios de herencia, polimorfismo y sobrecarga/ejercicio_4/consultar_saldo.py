from interfaz import InterfazEjecutarAccionUsuario
from clases_formulario import FormularioSiNo


class ConsultarSaldo(InterfazEjecutarAccionUsuario):
    
    def __init__(self):
        self.lista_opciones = None
        self.respuestas = {
            'si': Consultar(),
            'no': NoConsultarSaldo(),
        }
     
    
    def ejecutar(self, data, objeto):
        
        formulario = FormularioSiNo()
        formulario.mostrar(objeto)
        
        opcion_usuario = formulario.get_obtener_datos()
        
        if opcion_usuario in self.respuestas:
            self.respuestas[opcion_usuario].ejecutar(data, objeto)
        else:
            print('\n-Respuesta no valida')    
 
        
class Consultar(InterfazEjecutarAccionUsuario):
    
    def ejecutar(self, data, objeto):
        
        data.get_consultar_saldo()
              

class NoConsultarSaldo(InterfazEjecutarAccionUsuario):
    
    def ejecutar(self, data, objeto):
        print(f'\n---- No se consulto el saldo ---')
        