from interfaz import InterfazEjecutarAccionUsuario
from clases_formulario import FormularioSiNo
from logica_descuento_formulario import FormularioDescuentoProducto
from ejecutar_accion import RealizarFormulario, RealizarTransaccion

class AgregarDescuento(InterfazEjecutarAccionUsuario):
    
    def __init__(self):
        self.lista_opciones = None
        self.respuestas = {
            'si': ObtenerDatosDescuento(),
            'no': NoAplicarDescuento(),
        }
     
    
    def ejecutar(self, data, objeto):
        
        # fomulario si o no para hacer el descuento
        formulario = FormularioSiNo()
        formulario.mostrar(objeto)
        
        opcion_usuario = formulario.get_obtener_datos()
        
        if opcion_usuario in self.respuestas:
            self.respuestas[opcion_usuario].ejecutar(data, objeto)
        else:
            print('\n-Respuesta no valida')
        
 
        
class ObtenerDatosDescuento(InterfazEjecutarAccionUsuario):
    
    def ejecutar(self, data, objeto):
        
        lista_opciones = ['producto', 'descuento']
        # inyeccion de dependencias 
        formulario_descuento = FormularioDescuentoProducto()
        realizar_descuento = RealizarFormulario(formulario_descuento)
        realizar_descuento.obtener_lista_opciones(lista_opciones)
        realizar_descuento.realizar_formulario(objeto)
        datos_descuento = realizar_descuento.get_datos()
        
        # inyeccion de dependencias
        aplicar_descuento = AplicarDescuento()
        realizar_operacion = RealizarTransaccion(aplicar_descuento)
        realizar_operacion.realizar_transaccion(data, datos_descuento)


class AplicarDescuento(InterfazEjecutarAccionUsuario):
    
    def ejecutar(self, data, objeto):
        data.aplicar_descuento(objeto)    


class NoAplicarDescuento(InterfazEjecutarAccionUsuario):
    
    def ejecutar(self, data, objeto):
        print(f'\n---- No se aplico el descuento ---')
        