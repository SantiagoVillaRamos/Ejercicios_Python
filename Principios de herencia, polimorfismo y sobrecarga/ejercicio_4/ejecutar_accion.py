from interfaz import InterfazCuentaBancaria, InterfazOpciones, InterfazEjecutarAccionUsuario, InterfazEjecutarAccion, InterfazFormulario


class ServivioCuentaBancaria:
    
    """clase de alto nivel """
    
    def __init__(self, datos: InterfazCuentaBancaria):
        self.cuenta_bancaria = datos
        
    def set_agregar_saldo(self, datos):
        return self.cuenta_bancaria.set_agregar_saldo(datos)
        
    def depositar(self, monto):
        return self.cuenta_bancaria.depositar(monto)
        
    def retirar(self, monto):
        return self.cuenta_bancaria.retirar(monto)
    
    
    def get_consultar_saldo(self):
        print("\n--- Saldo Cuenta ---")
        saldo =  self.cuenta_bancaria.get_consultar_saldo()
        print(f" ---  ${saldo:.2f}")
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