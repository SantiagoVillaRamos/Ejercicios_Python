from interfaz import InterfazEmpleado, InterfazOpciones, InterfazEjecutarAccionUsuario, InterfazEjecutarAccion, InterfazFormulario


class ServivioEmpleado:
    
    """clase de alto nivel """
    
    def __init__(self, datos: InterfazEmpleado):
        self.datos_persona = datos
        
    def agregar_datos_persona(self, datos):
        return self.datos_persona.agregar_datos_persona(datos)
        
    def set_nombre_nuevo(self, nombre_persona, nuevo_nombre):
        return self.datos_persona.set_nombre_nuevo(nombre_persona, nuevo_nombre)
        
    def aumentar_salario(self, nombre_persona, aumento):
        return self.datos_persona.aumentar_salario(nombre_persona, aumento)
    
    def set_nuevo_salario(self, nombre_persona, nuevo_salario):
        return self.datos_persona.set_nuevo_salario(nombre_persona, nuevo_salario)
    
    def get_nombre(self):
        return self.datos_persona.get_nombre()
    
    def lista_empleados(self):
        print("\n--- Lista de Empleados ---")
        for persona in self.datos_persona.get_lista_empleados():
            print(f"{persona['nombre']}: ${persona['salario']:,}")
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