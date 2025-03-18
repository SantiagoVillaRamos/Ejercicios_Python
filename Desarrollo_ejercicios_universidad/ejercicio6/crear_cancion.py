from interfaz import Opcion
from clases_formularios import TituloCancion, ArtistaCancion, DuracionCancion
    
class CrearCancion(Opcion):
    
    def __init__(self):
        self.__objeto = None
    
    def ejecutar(self, playlist, objeto):
        
        validar_texto = objeto['validar_texto']
        validador_de_numero = objeto['validador_numero']
        
        titulo_cancion = TituloCancion()
        titulo_cancion.campo_formulario(validar_texto)
        titulo_de_cancion = titulo_cancion.get_titulo_cancion()
            
        nombre_del_artista = ArtistaCancion()
        nombre_del_artista.campo_formulario(validar_texto)
        nombre_artista = nombre_del_artista.get_nombre_artista()
                
        duracion_cancion = DuracionCancion()
        duracion_cancion.campo_formulario(validador_de_numero)
        numero_validado = duracion_cancion.get_duracion()
        
        self.__objeto = {'titulo_de_cancion': titulo_de_cancion, 'nombre_artista': nombre_artista,'duracion_cancion': numero_validado}
        
        logica_crear_cancion = LogicaCrearCancion()
        logica_crear_cancion.crear_cancion(playlist, self.get_objeto_cancion(), titulo_de_cancion)
        
    def get_objeto_cancion(self):
        return self.__objeto
 
 
class LogicaCrearCancion:
    def crear_cancion(self, crear_cancion_playlist, cancion, titulo_de_cancion):
        
        if crear_cancion_playlist.agrear_cancion(cancion):
            print(f'\nLa Cancion "{titulo_de_cancion}" se guardo')
        else:
            print(f'\nNo se guardo')
        
        print(f'\nLa duracion total de las canciones es: {crear_cancion_playlist.duracion_total_de_cancion()} minutos')
                              