from interfaz import InterfazEjecutarAccionUsuario
from logica_formulario_producto_y_precio import Formulario
from ejecutar_accion import RealizarFormulario, RealizarTransaccion


class ProductoPrecio(InterfazEjecutarAccionUsuario):
    
    def ejecutar(self, data, objeto):
        
        lista_opciones = ['producto', 'precio']
        # inyeccion de dependencias, formulario
        formulario = Formulario()
        realizar_formulario = RealizarFormulario(formulario)
        realizar_formulario.obtener_lista_opciones(lista_opciones)
        realizar_formulario.realizar_formulario(objeto)
        datos = realizar_formulario.get_datos()
        
        # inyeccion de dependencias, guardar los datos
        guardar_datos = GuardarDatos()
        accion = RealizarTransaccion(guardar_datos)
        accion.realizar_transaccion(data, datos)
         

class GuardarDatos(InterfazEjecutarAccionUsuario):
    
    def ejecutar(self, data, objeto):
       data.agregar_producto(objeto)
        

        