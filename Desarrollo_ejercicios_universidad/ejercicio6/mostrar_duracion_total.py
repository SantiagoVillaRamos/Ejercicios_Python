
from interfaz import Opcion, EjecutarOpcion
from clases_formularios import FormularioSalirDelPrograma

class MostrarDuracionTotal(Opcion):
    
    def __init__(self):
        self.opciones_usuario = {
            'si':OpcionSi(),
            'no':OpcionNo(),
        }
    
    def ejecutar(self, playlist, objeto_validadores):
        validar_texto = objeto_validadores['validar_texto']
        
        opcion_usuario = FormularioSalirDelPrograma()
        opcion_usuario.campo_formulario(validar_texto)
        
        opcion = self.opciones_usuario.get(opcion_usuario.get_salir()) 
        
        if opcion:
            opcion.ejecutar_opcion(playlist)
        else:
            print('\n-Opcion no valida')
    
    
class OpcionSi(EjecutarOpcion):
    def ejecutar_opcion(self, playlist):
        print(f'\n--Gracias por participar. Duracion de las canciones "{playlist.duracion_total_de_cancion()}"--')
        exit()


class OpcionNo(EjecutarOpcion):
    def ejecutar_opcion(self, playlist):
        print(f'\nDuracion de las canciones "{playlist.duracion_total_de_cancion()}"')
