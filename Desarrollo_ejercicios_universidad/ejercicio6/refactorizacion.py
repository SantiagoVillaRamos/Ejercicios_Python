from interfaz import Opcion, RealizarAccion
from clases_formularios import TituloCancion, ArtistaCancion, DuracionCancion
from ejecutar_accion import EjecutarAccion

    
class Formulario:
    def __init__(self, valores):
        self.valores = valores
        self.respuestas = {
            'titulo_cancion':TituloCancion(),
            'nombre_artista':ArtistaCancion(),
            'duracion_cancion':DuracionCancion()
        }
        self.__datos = {}
    
    def preguntar(self, validadores):
        
        # Verificar si todas las claves de respuestas están en la lista de valores
        if all(clave in self.valores for clave in self.respuestas.keys()):
            # Preguntar al usuario por cada atributo
            for clave, instancia in self.respuestas.items():
                print(f"\nPreguntando por: {clave}")
                instancia.campo_formulario(validadores)
                self.__datos[clave] = instancia.get_valor()
        else:
            print('\n-Opción no válida')

    def get_datos(self):
        return self.__datos
    

class Crear(Opcion):
    
    def ejecutar(self, playlist, objeto_validadores):
        
        lista_opciones_usuario = ['titulo_cancion', 'nombre_artista', 'duracion_cancion']
        formulario = Formulario(lista_opciones_usuario)
        formulario.preguntar(objeto_validadores)
        cancion_creada = formulario.get_datos()
        
        # inyeccion de dependencias para ejecutar la accion de agregar la cancion en la playlist    
        agregar_cancion = AgregarCancion()
        ejecutar_accion_agregar_cancion = EjecutarAccion(agregar_cancion)
        ejecutar_accion_agregar_cancion.ejecutar_accion(playlist, cancion_creada, cancion_creada['titulo_cancion'])
     
 
class AgregarCancion(RealizarAccion):
    
    def realizar_accion(self, accion_objeto_uno, accion_objeto_dos, accion_objeto_tres):
        
        if accion_objeto_uno.agrear_cancion(accion_objeto_dos):
            print(f'\nLa Cancion "{accion_objeto_tres}" se guardo')
        else:
            print(f'\nNo se guardo')
        
        print(f'\nLa duracion total de las canciones es: {accion_objeto_uno.duracion_total_de_cancion()} minutos')