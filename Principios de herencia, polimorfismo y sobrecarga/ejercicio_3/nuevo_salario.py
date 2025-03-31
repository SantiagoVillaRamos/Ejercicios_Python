from interfaz import InterfazEjecutarAccionUsuario
from clases_formulario import FormularioSiNo
from logica_formulario import Formulario
from ejecutar_accion import RealizarFormulario, RealizarOperacion

class AumentarSalarioEmpleado(InterfazEjecutarAccionUsuario):
    
    def __init__(self):
        self.lista_opciones = None
        self.respuestas = {
            'si': AumentoSalario(),
            'no': NoAplicarAumento(),
        }
     
    
    def ejecutar(self, data, objeto):
        
        formulario = FormularioSiNo()
        formulario.mostrar(objeto)
        
        opcion_usuario = formulario.get_obtener_datos()
        
        if opcion_usuario in self.respuestas:
            self.respuestas[opcion_usuario].ejecutar(data, objeto)
        else:
            print('\n-Respuesta no valida')
        
 
        
class AumentoSalario(InterfazEjecutarAccionUsuario):
    
    def ejecutar(self, data, objeto):
        
        lista_opciones = ['nombre', 'salario']
        # inyeccion de dependencias 
        formulario = Formulario()
        realizar_aumento = RealizarFormulario(formulario)
        realizar_aumento.obtener_lista_opciones(lista_opciones)
        realizar_aumento.realizar_formulario(objeto)
        datos = realizar_aumento.get_datos()
        
        # inyeccion de dependencias
        aplicar_aumento = AplicarAumento()
        realizar_operacion = RealizarOperacion(aplicar_aumento)
        realizar_operacion.realizar_operacion(data, datos)



class AplicarAumento(InterfazEjecutarAccionUsuario):
    
    def ejecutar(self, data, objeto): 
        data.set_nuevo_salario(objeto['nombre'], objeto['salario'])
            
        

class NoAplicarAumento(InterfazEjecutarAccionUsuario):
    
    def ejecutar(self, data, objeto):
        print(f'\n---- No se aplico el aumento de sueldo ---')
        