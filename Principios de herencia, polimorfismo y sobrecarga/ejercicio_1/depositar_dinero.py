from interfaz import InterfazEjecutarAccionUsuario
from logica_formulario_depositar import FormularioDepositarDineroUsuario
from ejecutar_accion import RealizarFormulario, RealizarTransaccion


class DepositarDinero(InterfazEjecutarAccionUsuario):
    
    def ejecutar(self, data, objeto):
        
        lista_opciones = ['depositar']
        # inyeccion de dependencias para el formulario
        formulario = FormularioDepositarDineroUsuario()
        realizar_formulario = RealizarFormulario(formulario)
        realizar_formulario.obtener_lista_opciones(lista_opciones)
        realizar_formulario.realizar_formulario(objeto)
        datos = realizar_formulario.get_datos()
        
        # inyeccion de dependencias para guardar los datos
        guardar_datos = GuardarDatosDepositar()
        accion = RealizarTransaccion(guardar_datos)
        accion.realizar_transaccion(data, datos)


class GuardarDatosDepositar(InterfazEjecutarAccionUsuario):
    
    def ejecutar(self, data, objeto):
        data.depositar(objeto['depositar'])
        