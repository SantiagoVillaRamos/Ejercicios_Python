from interfaz import InterfazEjecutarAccionUsuario
from logica_formulario import Formulario
from ejecutar_accion import RealizarFormulario, RealizarOperacion


class AgregarDatosPersona(InterfazEjecutarAccionUsuario):
    
    def ejecutar(self, data, objeto):
        
        lista_opciones = ['nombre', 'salario']
        # inyeccion de dependencias, formulario
        formulario = Formulario()
        realizar_formulario = RealizarFormulario(formulario)
        realizar_formulario.obtener_lista_opciones(lista_opciones)
        realizar_formulario.realizar_formulario(objeto)
        datos = realizar_formulario.get_datos()
        
        # inyeccion de dependencias, guardar los datos
        guardar_datos = GuardarDatos()
        accion = RealizarOperacion(guardar_datos)
        accion.realizar_operacion(data, datos)
        

class GuardarDatos(InterfazEjecutarAccionUsuario):
    
    def ejecutar(self, data, objeto):
        data.agregar_datos_persona(objeto)
         

        
        