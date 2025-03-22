from clases_formularios import TituloCancion, ArtistaCancion, DuracionCancion
from interfaz import RealizarAccionOpcion

class Formulario(RealizarAccionOpcion):
    def __init__(self, valores):
        self.valores = valores
        self.respuestas = {
            'titulo_cancion':TituloCancion(),
            'nombre_artista':ArtistaCancion(),
            'duracion_cancion':DuracionCancion()
        }
        self.__datos = {}
    
    def preguntar(self, dato):
        
        # Verificar si todas las claves de respuestas están en la lista de valores
        for valor in self.valores:
            if valor in self.respuestas:
                self.respuestas[valor].campo_formulario(dato)
                self.__datos[valor] = self.respuestas[valor].get_valor()
        else:
            print('\n-Opción no válida')

    def get_datos(self):
        return self.__datos