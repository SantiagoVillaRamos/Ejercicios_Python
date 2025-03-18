
from interfaz import Opcion, EjecutarOpcion
from clases_formularios import SalirDelPrograma

class MostrarDuracionTotal(Opcion):
    
    def __init__(self):
        self.opciones = {
            'si':OpcionSi(),
            'no':OpcionNo(),
        }
    
    def ejecutar(self, playlist, objeto):
        validar_texto = objeto['validar_texto']
        
        salir_del_programa = SalirDelPrograma()
        salir_del_programa.campo_formulario(validar_texto)
        
        opcion = self.opciones.get(salir_del_programa.get_salir()) 
        
        if opcion:
            opcion.ejecutar_opcion(playlist)
        else:
            print('\n-Opcion no valida')
    
    
class OpcionSi(EjecutarOpcion):
    def ejecutar_opcion(self, data):
        print(f'\n--Gracias por participar. Duracion de las canciones "{data.duracion_total_de_cancion()}--')
        exit()


class OpcionNo(EjecutarOpcion):
    def ejecutar_opcion(self, data):
        print(f'\nDuracion de las canciones "{data.duracion_total_de_cancion()}"')
