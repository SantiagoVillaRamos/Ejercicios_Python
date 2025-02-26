# Define una clase Playlist que contenga una lista de canciones.
# Cada canción puede representarse como un diccionario con
# atributos titulo, artista, y duracion. Agrega métodos
# agregar_cancion(cancion) y eliminar_cancion(titulo), así como
# duracion_total() que devuelva la duración total de todas las
# canciones. Crea una instancia de Playlist, añade y elimina
# canciones, y calcula la duración total.

from createDeleteUpdate import EliminarCancion, CrearCancion
from validadores import ValidadorDeTexto, ValidadorDeNumero

# clase playlist que tiene una lista de canciones
class Playlist:
    def __init__(self):
        self.__canciones = []
    
    # metodo que agrega una cancion a la lista
    def agregar_cancion(self, cancion):
        self.__canciones.append(cancion)
    
    # metodo que elimina una cancion de la lista
    def eliminar_cancion(self, titulo):
        for cancion in self.__canciones:
            if cancion['titulo'] == titulo:
                self.__canciones.remove(cancion)
            else:
                return False
        return titulo
    
    # metodo que devuelve la duracion total de las canciones
    def duracion_total(self):
        duracion = 0
        for cancion in self.__canciones:
            duracion += cancion['duracion']
        return duracion
    
    def get_play(self):
        return self.__canciones
 

# clase aplicacion que pide un titulo, un artista y una duracion y valida que sean correctos
class Aplicacion:
    def main():
        # se crea una lista de canciones vacia
        playlist = Playlist()
        
        while True:
        
            # se crea un menu con las opciones agregar cancion, eliminar cancion y salir
            opciones = ['Agregar cancion', 'Eliminar cancion', 'Salir']
            print('\nSelecciona una opcion:')
            for i, opcion in enumerate(opciones):
                print(f'{i+1}. {opcion}')
            # se pide una opcion y se valida que sea correcta
            while True:
                try:
                    opcion = int(input('\n---Opcion: '))
                    if opcion < 1 or opcion > 3:
                        raise ValueError('\n\tOpcion invalida')
                    break
                except ValueError as e:
                    print(e)
                    print('\t---Por favor, intenta de nuevo.---')
                    
            # si la opcion es 1 se pide un titulo, un artista y una duracion y se valida que sean correctos
            # se agrega la cancion a la lista y se imprime la duracion total de las canciones
            if opcion == 1:  
                cancion = CrearCancion()
                validar_texto = ValidadorDeTexto()
                validador_numero = ValidadorDeNumero()
                cancion.crear_cancion(playlist, validar_texto, validador_numero)

            # si la opcion es 2 se pide un titulo y se elimina la cancion de la lista y se imprime la duracion total de las canciones
            elif opcion == 2:
                eliminar_cancion = EliminarCancion()
                eliminar_cancion.eliminar_cancion_de_playlist(playlist)
                    
            # si la opcion es 3 se imprime la duracion total de las canciones y se sale del programa
            elif opcion == 3:
                print(f'\nLa duracion total de las canciones es: {playlist.duracion_total()} minutos')
                break                
        
# se llama a la clase aplicacion
if __name__ == '__main__':
    Aplicacion.main()