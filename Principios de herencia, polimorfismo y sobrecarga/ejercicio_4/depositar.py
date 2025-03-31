from interfaz import InterfazEjecutarAccionUsuario
from logica_formulario import Formulario
from ejecutar_accion import RealizarFormulario, RealizarOperacion


class Depositar(InterfazEjecutarAccionUsuario): 
    
    def ejecutar(self, data, objeto):
        
        lista_opciones = ['saldo']
        # inyeccion de dependencias para el formulario
        formulario = Formulario()
        realizar_formulario = RealizarFormulario(formulario)
        realizar_formulario.obtener_lista_opciones(lista_opciones)
        realizar_formulario.realizar_formulario(objeto)
        datos = realizar_formulario.get_datos()
        
        # inyeccion de dependencias, modificar nombre empleado
        depositar_cuenta = DepositarCuenta()
        accion = RealizarOperacion(depositar_cuenta)
        accion.realizar_operacion(data, datos)
        
               
class DepositarCuenta(InterfazEjecutarAccionUsuario):
    
    def ejecutar(self, data, objeto):
        
        data.depositar(objeto['saldo'])
            
        