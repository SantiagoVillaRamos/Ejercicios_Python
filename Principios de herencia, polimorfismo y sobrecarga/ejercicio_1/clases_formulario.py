from interfaz import InterfazFormulario


class FormularioDepositarDinero(InterfazFormulario):
    
    def __init__(self):
        self.__deposito_dinero = None
    
    def mostrar(self, data):
        validador_de_numero = data['validador_numero']
        while True:
            try:
                deposito_dinero = input('\nIngrese deposito de Dinero: ')
                monto_validado = validador_de_numero.validar(deposito_dinero)
                self.__deposito_dinero = monto_validado
                print(f'\n- $ {validador_de_numero.obtener_datos():,} valor valido')
                break
            except ValueError as e:
                print(f'\nError: {e}\n--- Por favor, intente de nuevo ---')
        
    def get_obtener_datos(self):
        return self.__deposito_dinero
    
    
      
class FormularioRetirarDinero(InterfazFormulario):
    
    def __init__(self):
        self.__retiro_dinero = None
    
    def mostrar(self, data):
        validador_de_numero = data['validador_numero']
        while True:
            try:
                retiro_dinero = input('\nIngrese retiro de Dinero: ')
                numero_validado = validador_de_numero.validar(retiro_dinero)
                self.__retiro_dinero = numero_validado
                print(f'-\n $ {validador_de_numero.obtener_datos():,} valor valido')
                break
            except ValueError as e:
                print(f'\nError: {e}\n--- Por favor, intente de nuevo ---')
        
    def get_obtener_datos(self):
        return self.__retiro_dinero
    
    

class FormularioSalirDelPrograma(InterfazFormulario):
    
    def __init__(self):
        self.__Salir_del_programa = None
    
    def mostrar(self, data):
        validar_texto = data['validador_texto']
        while True:
            try:
                salir = input('\n¿Estas seguro de salir ? (si/no): ')
                salir_del_programa = validar_texto.validar(salir)
                if salir_del_programa:
                    print(f'Titulo "{validar_texto.obtener_datos()}" valido')
                    self.__Salir_del_programa = salir_del_programa
                    break
            except ValueError as e:
                print(e)
                print('\t---Por favor, intenta de nuevo.---')
                
    def get_obtener_datos(self):
        return self.__Salir_del_programa