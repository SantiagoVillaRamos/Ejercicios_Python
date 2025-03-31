from interfaz import InterfazEjecutarAccionUsuario
from logica_formulario import Formulario
from ejecutar_accion import RealizarFormulario, RealizarOperacion


class Retirar(InterfazEjecutarAccionUsuario):
    
    def ejecutar(self, data, objeto):
        
        lista_opciones = ['saldo']
        # inyeccion de dependencias, formulario
        formulario = Formulario()
        realizar_formulario = RealizarFormulario(formulario)
        realizar_formulario.obtener_lista_opciones(lista_opciones)
        realizar_formulario.realizar_formulario(objeto)
        datos = realizar_formulario.get_datos()
        
        # inyeccion de dependencias, guardar los datos
        retirar = RetirarDeCuenta()
        accion = RealizarOperacion(retirar)
        accion.realizar_operacion(data, datos)
        

class RetirarDeCuenta(InterfazEjecutarAccionUsuario):
    
    def ejecutar(self, data, objeto):
        data.retirar(objeto['saldo'])
          
            
