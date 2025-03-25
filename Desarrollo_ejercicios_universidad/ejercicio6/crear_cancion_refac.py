from interfaz import Opcion, RealizarAccion
from ejecutar_accion import EjecutarAccion, RealizarAccionOpcionPrograma
from logica_formulario import Formulario


class CrearCancion(Opcion):
    
    def ejecutar(self, playlist, objeto_validadores):
        
        """Corregir la inyeccion de dependencias"""
        lista_opciones_usuario = ['titulo_cancion', 'nombre_artista', 'duracion_cancion']
        formulario = Formulario(lista_opciones_usuario)
        realizar_accion_opcion = RealizarAccionOpcionPrograma(formulario)
        realizar_accion_opcion.realizar_accion(objeto_validadores)
        cancion_creada = realizar_accion_opcion.get_datos()
        
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