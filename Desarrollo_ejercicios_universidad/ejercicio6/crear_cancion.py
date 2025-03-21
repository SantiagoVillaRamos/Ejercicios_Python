from interfaz import Opcion, RealizarAccion
from clases_formularios import TituloCancion, ArtistaCancion, DuracionCancion
from ejecutar_accion import EjecutarAccion

class CrearCancion(Opcion):
    
    def __init__(self):
        self.__objeto_cancion = None
    
    def ejecutar(self, playlist, objeto_validadores):
        
        validar_texto = objeto_validadores['validar_texto']
        validador_de_numero = objeto_validadores['validador_numero']
        
        titulo_cancion = TituloCancion()
        titulo_cancion.campo_formulario(validar_texto)
        titulo_de_cancion = titulo_cancion.get_titulo_cancion()
             
        nombre_del_artista = ArtistaCancion()
        nombre_del_artista.campo_formulario(validar_texto)
        nombre_artista = nombre_del_artista.get_nombre_artista()
                
        duracion_cancion = DuracionCancion()
        duracion_cancion.campo_formulario(validador_de_numero)
        duracion_de_cancion = duracion_cancion.get_duracion()
        
        self.__objeto_cancion = {'titulo_de_cancion': titulo_de_cancion, 'nombre_artista': nombre_artista,'duracion_cancion': duracion_de_cancion}
        
        # inyeccion de dependencias para ejecutar la accion de agregar la cancion en la playlist    
        agregar_cancion = AgregarCancion()
        ejecutar_accion_agregar_cancion = EjecutarAccion(agregar_cancion)
        ejecutar_accion_agregar_cancion.ejecutar_accion(playlist, self.get_objeto_cancion(), titulo_de_cancion)
        
    def get_objeto_cancion(self):
        return self.__objeto_cancion
     
 
class AgregarCancion(RealizarAccion):
    
    def realizar_accion(self, accion_objeto_uno, accion_objeto_dos, accion_objeto_tres):
        
        if accion_objeto_uno.agrear_cancion(accion_objeto_dos):
            print(f'\nLa Cancion "{accion_objeto_tres}" se guardo')
        else:
            print(f'\nNo se guardo')
        
        print(f'\nLa duracion total de las canciones es: {accion_objeto_uno.duracion_total_de_cancion()} minutos')
                              