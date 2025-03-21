# Define una clase Playlist que contenga una lista de canciones.
# Cada canción puede representarse como un diccionario con
# atributos titulo, artista, y duracion. Agrega métodos
# agregar_cancion(cancion) y eliminar_cancion(titulo), así como
# duracion_total() que devuelva la duración total de todas las
# canciones. Crea una instancia de Playlist, añade y elimina
# canciones, y calcula la duración total. 


from validadores import ValidadorDeTexto, ValidadorDeNumero
from playlist import Playlist, AlmacenamientoEnLista
from formulario_opcion_usuario import FormularioOpcionUsuario
from lista_opciones import ListaOpcionesAplicacion
from opcion_usuario import OpcionUsuario
from ejecutar_accion import EjecutarAccion

class AplicacionCancion:
    
    def main():
        # inyeccion de dependencias para la playlist
        almacenamiento_en_lista = AlmacenamientoEnLista()
        playlist = Playlist(almacenamiento_en_lista)
        objeto_validadores =  {
            'validar_texto': ValidadorDeTexto(),
            'validador_numero': ValidadorDeNumero()
        }
        
        while True:
        
            lista_de_opciones = ListaOpcionesAplicacion()
            lista_de_opciones.lista_opciones_aplicacion()
            
            formulario_opcion_usuario = FormularioOpcionUsuario()
            # inyeccion de dependencias para la opcion del usuario  
            opcion_usuario = OpcionUsuario()
            opciones_usuario = EjecutarAccion(opcion_usuario)
            
            if opciones_usuario.ejecutar_accion(formulario_opcion_usuario.formulario_opcion_usuario(), playlist, objeto_validadores):
                break
                 
# se llama la clase aplicacion que iniciara el programa
if __name__ == '__main__':
    AplicacionCancion.main()