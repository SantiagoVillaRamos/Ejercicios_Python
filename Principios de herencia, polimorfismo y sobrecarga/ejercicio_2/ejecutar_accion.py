from interfaz import InterfazProducto, InterfazOpciones, InterfazEjecutarAccionUsuario, InterfazEjecutarAccion, InterfazFormulario


# clase de alto nivel que depende de la abstraccion
class ServicioVentas:
    
    def __init__(self, producto: InterfazProducto):  # Depende de la abstracción
        self.producto = producto
        
    def agregar_producto(self, producto):
        return self.producto.agregar_producto(producto)

    def aplicar_descuento(self, objeto):
        return self.producto.aplicar_descuento(objeto)
        
    def actualizar_precio_producto(self, producto, nuevo_precio):
        return self.producto.set_precio(producto, nuevo_precio)
    
    def precio_producto(self):
        return self.producto.get_precio()
    
    def mostrar_productos(self):
        print("\n--- Lista de Productos ---")
        for producto in self.producto.mostrar_productos():
            print(f"{producto['producto']}: ${producto['precio']:,}")
        print("--------------------------")
    
    
# clase de alto nivel que realiza la acción seleccionada
class RealizarAccion:
    
    def __init__(self, accion: InterfazOpciones):
        self._accion = accion
        
    def realizar_accion_programa(self, opcion, data, objeto):
        self._accion.realizar_accion(opcion, data, objeto)
        

# clase de alto nivel que realiza la transacción seleccionada
class RealizarTransaccion:
    
    def __init__(self, transaccion: InterfazEjecutarAccionUsuario):
        self._transaccion = transaccion
        
    def realizar_transaccion(self, data, objeto):
        self._transaccion.ejecutar(data, objeto)
        
        
# clase de alto nivel que realiza el formulario de la opción seleccionada
class RealizarFormulario:
    
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