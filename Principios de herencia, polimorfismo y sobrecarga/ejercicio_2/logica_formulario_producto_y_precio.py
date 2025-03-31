
from clases_formulario import FormularioProducto, FormularioPrecioProducto
from interfaz import InterfazEjecutarAccion

""" Esta clase formulario se utiliza para registrar el producto y precio. 
    De igual manera, se reutiliza para actualizar el precio de un producto
    que este en la base de datos (en este caso la lista de diccionarios que esta
    en producto.py)

"""
class Formulario(InterfazEjecutarAccion):
    
    def __init__(self):
        self.__lista_opciones = None
        self.respuestas = {
            'producto': FormularioProducto(),
            'precio': FormularioPrecioProducto(),
        }
        self.__datos = {}
        
    def lista_opiones(self, lista_opciones):
        self.__lista_opciones = lista_opciones
        
        
    def ejecutar_accion_usuario(self, data):
        # Verificar si la clave de respuesta está en la lista de valores
        for valor in self.__lista_opciones:
            if valor in self.respuestas:
                self.respuestas[valor].mostrar(data)
                self.__datos[valor] = self.respuestas[valor].get_obtener_datos()
            else:
                print('\n-Opción no válida')

    def get_datos(self):
        return self.__datos 