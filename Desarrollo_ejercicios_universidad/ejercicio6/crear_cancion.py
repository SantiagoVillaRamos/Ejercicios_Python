from interfaz import Crear
from clases_formularios import TituloCancion, ArtistaCancion, DuracionCancion
from logica import LogicaCrearCancion
                              
                              
class CrearCancionEnPlaylist(Crear):
    
    def __init__(self):
        self.__objeto = None
    
    def crear_cancion(self, data):
        
        crear_cancion_playlist = data['playlist']
        validar_texto = data['validar_texto']
        validador_de_numero = data['validador_numero']
        
        
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
        logica_crear_cancion.crear_cancion(crear_cancion_playlist, self.get_objeto_cancion(), titulo_de_cancion)    

    
    def get_objeto_cancion(self):
        return self.__objeto
           