from interfaz import CampoFormulario


class TituloCancion(CampoFormulario):
    def __init__(self):
        self.__titulo_cancion = None
    
    def campo_formulario(self, data):
        validar_texto = data['validar_texto']
        while True:
            try: 
                titulo_de_cancion = input('\nIngresa el titulo de la cancion: ')
                titulo_cancion = validar_texto.validador_de_texto(titulo_de_cancion)
                if titulo_cancion:
                    print(f'Titulo "{validar_texto.get_texto()}" valido')
                    self.__titulo_cancion = titulo_cancion
                    break
            except ValueError as e:
                print(e)
                print('\t---Por favor, intenta de nuevo.---')
                
    def get_valor(self):
        return self.__titulo_cancion
    
    
class ArtistaCancion(CampoFormulario):
    def __init__(self):
        self.__nombre_artista = None
    
    def campo_formulario(self, data):
        validar_texto = data['validar_texto']
        while True:
            try:
                artista_de_cancion = input('\nIngresa el artista de la cancion: ')   
                nombre_artista = validar_texto.validador_de_texto(artista_de_cancion)           
                if nombre_artista:
                    print(f'Artista "{validar_texto.get_texto()}" valido')
                    self.__nombre_artista = nombre_artista
                    break
            except ValueError as e:
                print(e)
                print('\t---Por favor, intenta de nuevo.---')
                   
    def get_valor(self):
        return self.__nombre_artista
    
    
class DuracionCancion(CampoFormulario):
    def __init__(self):
        self.__duracion = None
    
    def campo_formulario(self, data):
        validador_de_numero = data['validador_numero']
        while True:
            try:
                duracion_de_cancion = int(input('\nIngresa la duracion de la cancion: '))
                numero_validado = validador_de_numero.validador_duracion_cancion(duracion_de_cancion)
                if numero_validado:
                    print(f'-"{validador_de_numero.get_numero()}" Duracion valida')
                    self.__duracion = numero_validado
                    break
                else:
                    print('\n--El numero no existe')
            except ValueError as e:
                print(e)
                print('\t---Por favor, intenta de nuevo.---')
        
    def get_valor(self):
        return self.__duracion
    
    
class FormularioSalirDelPrograma(CampoFormulario):
    def __init__(self):
        self.__Salir_del_programa = None
    
    def campo_formulario(self, data):
        validar_texto = data['validar_texto']
        while True:
            try:
                salir = input('\n¿Estas seguro de salir ? (si/no): ')
                salir_del_programa = validar_texto.validador_de_texto(salir)
                if salir_del_programa:
                    print(f'Titulo "{validar_texto.get_texto()}" valido')
                    self.__Salir_del_programa = salir_del_programa
                    break
            except ValueError as e:
                print(e)
                print('\t---Por favor, intenta de nuevo.---')
                
    def get_valor(self):
        return self.__Salir_del_programa