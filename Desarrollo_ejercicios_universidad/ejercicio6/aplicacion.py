# Define una clase Playlist que contenga una lista de canciones.
# Cada canción puede representarse como un diccionario con
# atributos titulo, artista, y duracion. Agrega métodos
# agregar_cancion(cancion) y eliminar_cancion(titulo), así como
# duracion_total() que devuelva la duración total de todas las
# canciones. Crea una instancia de Playlist, añade y elimina
# canciones, y calcula la duración total. 


from validadores import ValidadorDeTexto, ValidadorDeNumero
from playlist import Playlist
from formulario_opcion_usuario import FormularioOpcionUsuario
from lista_opciones import ListaOpciones
from opcion_usuario import OpcionUsuario

# clase aplicacion
class Aplicacion:
    
    def main():
        
        playlist = Playlist()
        validar_texto = ValidadorDeTexto()
        validador_numero = ValidadorDeNumero()
        objeto =  {
            'playlist':playlist,
            'validar_texto': validar_texto,
            'validador_numero': validador_numero
        }
        
        while True:
        
            lista_de_opciones = ListaOpciones()
            lista_de_opciones.lista_opciones()
            print(playlist.get_canciones())
            
            formulario_opcion_usuario = FormularioOpcionUsuario()
            
            opciones_usuario = OpcionUsuario()
            if opciones_usuario.opciones_usuario(formulario_opcion_usuario.formulario_opcion_usuario(), playlist, objeto) == 4:
                break  


# se llama a la clase aplicacion
if __name__ == '__main__':
    Aplicacion.main()