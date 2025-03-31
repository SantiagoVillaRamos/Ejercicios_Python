from interfaz import InterfazValidadores

class ValidadorNumero(InterfazValidadores):
    def __init__(self):
        self._numero = None
        
    def validar(self, data):

        if not data:
            raise ValueError("\nEl campo no puede estar vacío")
            
        # Validación 2: Es convertible a número
        try:
            numero_valido = int(data)
        except ValueError:
            raise ValueError("\nDebe ingresar un número entero válido")
        
        if numero_valido <= 0:
            raise ValueError("\nEl monto debe ser positivo")
        
        self._numero = numero_valido
        return self._numero
        
    def obtener_datos(self):
        return self._numero
       
       
# validador texto
class ValidadorDeTexto(InterfazValidadores):
    def __init__(self):
        self._texto = '' 
        
    def validar(self, data):
        if not data.strip():
            raise ValueError(f'\t---La cadena de texto no puede estar vacío')
        if any(char.isdigit() for char in data):
            raise ValueError(f'\t---"{data}": no puede contener números')
        self._texto = data
        return self._texto
        
    def obtener_datos(self):
        return self._texto
    
    
class LimitesDescuentos(InterfazValidadores):
     
    def __init__(self):
        self._valor = None
        
    def validar(self, data):
        if data > 50:
            raise ValueError(f'\n---El descuento debe ser menor a 50%')
        self._valor = data
        return self._valor
    
    def obtener_datos(self):
        return self._valor
    

class Limites(InterfazValidadores):
    
    """valida que el valor ingresado este en la lista de opciones"""
    
    def __init__(self):
        self._valor = None
        
    def validar(self, data):
        lista_numero_opciones = [1, 2, 3, 4, 5]
        if data not in lista_numero_opciones:
            raise ValueError('\n\tOpcion invalida')
        self._valor = data
        return self._valor
    
    def obtener_datos(self):
        return self._valor