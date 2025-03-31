
from interfaz import InterfazFormulario

class FormularioOpcionUsuario(InterfazFormulario):
    
    """Encargado de preguntar por las opciones predeterminadas"""
    
    def __init__(self):
        self._numero = None
    
    def mostrar(self, data):
        
        validar_numero = data['validador_numero']
        validar_limites = data['validar_limites']
        while True:
            try:
                opcion = input('\n---Opcion: ') 
                numero_validado = validar_numero.validar(opcion)
                numero_limite = validar_limites.validar(numero_validado)
                print(f"Valor validado: {numero_limite}")
                self._numero = numero_limite
                break
            except ValueError as e:
                print(e)
                print('\t---Por favor, intenta de nuevo.---')
        
    def get_obtener_datos(self):
        return self._numero
