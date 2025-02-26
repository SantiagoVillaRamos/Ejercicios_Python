# clase que valida que la cadena no este vacia y no tenga numeros
class ValidadorDeTexto:
    def __init__(self):
        self.__texto = ''
        
    def validador_de_texto(self, texto):
        if not texto.strip():
            raise ValueError(f'\t---La cadena de texto no puede estar vacío')
        if any(char.isdigit() for char in texto):
            raise ValueError(f'\t---"{texto}": no puede contener números')
        self.__texto = texto
        return self.__texto
        
    def get_nombre(self):
        return self.__texto


# clase que valida que el numero sea mayor a 0
class ValidadorDeNumero:
    def __init__(self):
        self.__numero = int()
        
    def validador_numero(self, numero):
        if numero <= 0:
            raise ValueError(f'\nDuracion: "{numero}". Debe ser mayor a 0')
        elif numero > 7:
            raise ValueError(f'\tDuracion: "{numero}". Debe ser menor a 7 minutos')
        self.__numero = numero
        return self.__numero
        
    def get_numero(self):
        return self.__numero