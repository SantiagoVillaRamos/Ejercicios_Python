from interfaz import InterfazPuntos, InterfazOpciones, InterfazEjecutarAccionUsuario, InterfazEjecutarAccion, InterfazFormulario


class ServivioPuntuacion:
    
    """clase de alto nivel """
    
    def __init__(self, datos: InterfazPuntos):
        self.marca = datos
        
    def agregar_puntos(self, datos):
        return self.marca.agregar_puntos(datos)
        
    def restar_puntos(self, puntos):
        return self.marca.restar_puntos(puntos)
    
    def get_consultar_puntuacion(self):
        print("\n --- Marcas ---")
        print(f" --- Puntos: {self.marca.get_consultar_puntuacion()}")
        print("--------------------------")
    
    

class RealizarAccion:
    
    """clase de alto nivel que realiza la acción seleccionada"""
    
    def __init__(self, accion: InterfazOpciones):
        self._accion = accion
        
    def realizar_accion_programa(self, opcion, data, objeto):
        self._accion.realizar_accion(opcion, data, objeto)
       
      

class RealizarOperacion:
    
    """clase de alto nivel que realiza la transacción seleccionada"""
    
    def __init__(self, operacion: InterfazEjecutarAccionUsuario):
        self.operacion = operacion
        
    def realizar_operacion(self, data, objeto):
        self.operacion.ejecutar(data, objeto)
        
        

class RealizarFormulario:
    
    """clase de alto nivel que realiza el formulario de la opción seleccionada"""
    
    def __init__(self, formulario: InterfazEjecutarAccion):
        self._formulario = formulario
        
    def obtener_lista_opciones(self, lista_opciones):
        self._formulario.lista_opiones(lista_opciones)
        
    def realizar_formulario(self, data):
        self._formulario.ejecutar_accion_usuario(data)
        
    def get_datos(self):
        return self._formulario.get_datos()
    
  
class RealizarOpcion:
    
    """Clase de alto nivel"""
    
    def __init__(self, opcion: InterfazFormulario):
        self.opcion = opcion
        
    def realizar_opcion(self, data):
        self.opcion.mostrar(data)
        
    def mostrar_opcion(self):
        return self.opcion.get_obtener_datos()