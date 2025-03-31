
from interfaz import InterfazOpciones, InterfazEjecutarAccion, InterfazBanco, InterfazEjecutarAccionUsuario, InterfazFormulario

"""clases de alto nivel que manejan la ejecución de las acciones del programa"""

# clase que realiza la acción seleccionada
class RealizarAccion:
    
    def __init__(self, accion: InterfazOpciones):
        self._accion = accion
        
    def realizar_accion_programa(self, opcion, data, objeto):
        self._accion.realizar_accion(opcion, data, objeto)
        
        
# clase que realiza el formulario de la opción seleccionada
class RealizarFormulario:
    
    def __init__(self, formulario: InterfazEjecutarAccion):
        self._formulario = formulario
        
    def obtener_lista_opciones(self, lista_opciones):
        self._formulario.lista_opiones(lista_opciones)
        
    def realizar_formulario(self, data):
        self._formulario.ejecutar_accion_usuario(data)
        
    def get_datos(self):
        return self._formulario.get_datos()
    
    
# clase que maneja la lógica de negocio del banco
class BancoNegocio:
    
    def __init__(self, data: InterfazBanco):
        self.data = data
        
    def depositar(self, cantidad):
        return self.data.depositar(cantidad)
        
    def retirar(self, cantidad):
        return self.data.retirar(cantidad)
        
    def obtener_balance(self):
        print(f"""
              --------------
              Balance Cuenta: $ {self.data.obtener_balance():,}
              ---------------
        """)
        
    

# clase que realiza la transacción seleccionada
class RealizarTransaccion:
    
    def __init__(self, transaccion: InterfazEjecutarAccionUsuario):
        self._transaccion = transaccion
        
    def realizar_transaccion(self, data, objeto):
        self._transaccion.ejecutar(data, objeto)
        
        
class RealizarOpcion:
    
    """Clase de alto nivel"""
    
    def __init__(self, opcion: InterfazFormulario):
        self.opcion = opcion
        
    def realizar_opcion(self, data):
        self.opcion.mostrar(data)
        
    def mostrar_opcion(self):
        return self.opcion.get_obtener_datos()