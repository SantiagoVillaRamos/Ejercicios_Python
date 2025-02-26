
# clase que maneja la logica de eliminar cancion
class EliminarCancion:
    def eliminar_cancion_de_playlist(self, playlist):
        titulo = input('\nIngresa el titulo de la cancion a eliminar: ')
        titulo_cancion = playlist.eliminar_cancion(titulo)
        if titulo_cancion != titulo:
            print(f'\n---La cancion "{titulo}" no se encuentra en la lista---')
            print(f'\n-La duracion total de las canciones es: {playlist.duracion_total()} minutos-')
        else:
            print(f'\nLa cancion "{titulo}" ha sido eliminada de la lista')
            print(f'\nLa duracion total de las canciones es: {playlist.duracion_total()} minutos')
            
            
# clase que maneja la logica de la opcion 1
class CrearCancion:
    def crear_cancion(self, playlist, validar_texto, validador_de_numero):
        while True:
            try:
                titulo = input('\nIngresa el titulo de la cancion: ')
                titulo_cancion = validar_texto.validador_de_texto(titulo)
                if titulo_cancion:
                    print(f'Titulo "{validar_texto.get_nombre()}" valido')
                    break
            except ValueError as e:
                print(e)
                print('\t---Por favor, intenta de nuevo.---')
            
        while True:
            try:
                artista = input('\nIngresa el artista de la cancion: ')   
                nombre_artista = validar_texto.validador_de_texto(artista)               
                if nombre_artista:
                    print(f'Artista "{validar_texto.get_nombre()}" valido')
                    break
            except ValueError as e:
                print(e)
                print('\t---Por favor, intenta de nuevo.---')
                
        while True:
            try:
                duracion = int(input('\nIngresa la duracion de la cancion: '))
                if validador_de_numero.validador_numero(duracion):
                    print('Duracion valida')
                    break
            except ValueError as e:
                print(e)
                print('\t---Por favor, intenta de nuevo.---')
        
        cancion = {'titulo': titulo_cancion, 'artista': nombre_artista, 'duracion': validador_de_numero.get_numero()}
        playlist.agregar_cancion(cancion)
        print(f'\nLa duracion total de las canciones es: {playlist.duracion_total()} minutos')