from interfaz import InterfazEjecutarAccionUsuario
from logica_formulario_producto_y_precio import Formulario
from ejecutar_accion import RealizarFormulario, RealizarTransaccion


class ActualizarPrecio(InterfazEjecutarAccionUsuario): 
    
    def ejecutar(self, data, objeto):
        
        lista_opciones = ['producto', 'precio']
        # inyeccion de dependencias para el formulario
        formulario = Formulario()
        realizar_formulario = RealizarFormulario(formulario)
        realizar_formulario.obtener_lista_opciones(lista_opciones)
        realizar_formulario.realizar_formulario(objeto)
        datos = realizar_formulario.get_datos()
        
        # inyeccion de dependencias, modificar precio
        modificar_precio = ModificarPrecio()
        accion = RealizarTransaccion(modificar_precio)
        accion.realizar_transaccion(data, datos)
        
               
class ModificarPrecio(InterfazEjecutarAccionUsuario):
    
    def ejecutar(self, data, objeto):
        
        data.actualizar_precio_producto(objeto['producto'], objeto['precio'])
        