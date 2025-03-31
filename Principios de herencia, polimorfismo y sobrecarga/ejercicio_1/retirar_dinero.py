from interfaz import InterfazEjecutarAccionUsuario, InterfazEjecutarAccionUsuario
from logica_formulario_retirar import FormularioRetirarDineroUsuario
from ejecutar_accion import RealizarFormulario, RealizarTransaccion


class RetirarDinero(InterfazEjecutarAccionUsuario):
    
    def ejecutar(self, data, objeto):
        
        lista_opciones = ['retirar']
        # inyeccion de dependencias para el formulario
        formulario = FormularioRetirarDineroUsuario()
        realizar_formulario = RealizarFormulario(formulario)
        realizar_formulario.obtener_lista_opciones(lista_opciones)
        realizar_formulario.realizar_formulario(objeto)
        datos = realizar_formulario.get_datos()
        
        # inyeccion de dependencias para guardar los datos
        guardar_datos = GuardarDatosRetirar()
        accion = RealizarTransaccion(guardar_datos)
        accion.realizar_transaccion(data, datos)
        
        
class GuardarDatosRetirar(InterfazEjecutarAccionUsuario):
    
    def ejecutar(self, data, objeto):
        data.retirar(objeto['retirar'])
