from interfaz import InterfazEjecutarAccionUsuario

class ListaProducto(InterfazEjecutarAccionUsuario):
    
    def ejecutar(self, data, objeto):
        
        data.mostrar_productos()