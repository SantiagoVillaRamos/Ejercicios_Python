from interfaz import InterfazVehiculo, InterfazOpciones, InterfazEjecutarAccionUsuario, InterfazEjecutarAccion, InterfazFormulario


class ServivioVehiculo:
    
    """clase de alto nivel """
    
    def __init__(self, datos: InterfazVehiculo):
        self.marca = datos
        
    def agregar_datos(self, datos):
        return self.marca.agregar_datos(datos)
        
    def set_velocidad_maxima(self, nombre, nueva_velocidad):
        return self.marca.set_velocidad_maxima(nombre, nueva_velocidad)
    
    def get_marca(self):
        print("\n --- Marcas ---")
        for marca in self.marca.get_marca():
            print(f" ---Vehiculo: {marca['nombre']} | Velocidad: {marca['velocidad']} k/lh")
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