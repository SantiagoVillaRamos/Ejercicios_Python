
from interfaz import InterfazOpciones
from producto_precio import ProductoPrecio
from actualizar_precio import ActualizarPrecio
from agregar_descuento import AgregarDescuento
from lista_productos import ListaProducto
from salir import Salir

class OpcionesUsuario(InterfazOpciones):
    
    # Mapeo de opciones a clases
    def __init__(self):
        self.opciones_de_usuario = {
            1:ProductoPrecio(),
            2:ActualizarPrecio(),
            3:AgregarDescuento(),
            4:ListaProducto(),
            5:Salir(),
        }
     
    def realizar_accion(self, opcion, data, objeto):
        
        opcion_usuario = self.opciones_de_usuario.get(opcion)
        
        if opcion_usuario:
            opcion_usuario.ejecutar(data, objeto)
        else:
            print('\n-Opcion no valida')