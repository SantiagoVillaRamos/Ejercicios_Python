from interfaz import InterfazEjecutarAccionUsuario
from logica_formulario import FormularioNombreNuevo
from ejecutar_accion import RealizarFormulario, RealizarOperacion


class NuevoNombreEmpleado(InterfazEjecutarAccionUsuario): 
    
    def ejecutar(self, data, objeto):
        
        lista_opciones = ['nombre', 'nuevo_nombre']
        # inyeccion de dependencias para el formulario
        formulario = FormularioNombreNuevo()
        realizar_formulario = RealizarFormulario(formulario)
        realizar_formulario.obtener_lista_opciones(lista_opciones)
        realizar_formulario.realizar_formulario(objeto)
        datos = realizar_formulario.get_datos()
        
        # inyeccion de dependencias, modificar nombre empleado
        nombre_nuevo = NombreNuevoEmpleado()
        accion = RealizarOperacion(nombre_nuevo)
        accion.realizar_operacion(data, datos)
        
               
class NombreNuevoEmpleado(InterfazEjecutarAccionUsuario):
    
    def ejecutar(self, data, objeto):
        
        data.set_nombre_nuevo(objeto['nombre'], objeto['nuevo_nombre'])
            
        