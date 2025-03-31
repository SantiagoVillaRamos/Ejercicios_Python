from interfaz import InterfazEjecutarAccionUsuario
from logica_formulario import Formulario
from ejecutar_accion import RealizarFormulario, RealizarOperacion


class RestarPuntosJuego(InterfazEjecutarAccionUsuario): 
    
    def ejecutar(self, data, objeto):
        
        lista_opciones = ['puntos']
        # inyeccion de dependencias para el formulario
        formulario = Formulario()
        realizar_formulario = RealizarFormulario(formulario)
        realizar_formulario.obtener_lista_opciones(lista_opciones)
        realizar_formulario.realizar_formulario(objeto)
        datos = realizar_formulario.get_datos()
        
        # inyeccion de dependencias, modificar nombre empleado
        restar_puntos = RestarPuntos()
        accion = RealizarOperacion(restar_puntos)
        accion.realizar_operacion(data, datos)
        
               
class RestarPuntos(InterfazEjecutarAccionUsuario):
    
    def ejecutar(self, data, objeto):
        if isinstance(objeto, dict):
            if 'puntos' not in objeto:
                print("Error: El diccionario no contiene la clave 'puntos'")
                return False
        data.restar_puntos(objeto['puntos'])
            
        