from interfaz import InterfazFormulario


class FormularioProducto(InterfazFormulario):
    
    def __init__(self):
        self.__nombre_producto = None
    
    def mostrar(self, data):
        validador_de_texto = data['validador_texto']
        while True:
            try:
                nombre_producto = input('\nNombre del producto: ')
                monto_validado = validador_de_texto.validar(nombre_producto)
                self.__nombre_producto = monto_validado
                print(f'-"{validador_de_texto.obtener_datos()}" valido')
                break
            except ValueError as e:
                print(f'\nError: {e}\n--- Por favor, intente de nuevo ---')
        
    def get_obtener_datos(self):
        return self.__nombre_producto
    
    
      
class FormularioPrecioProducto(InterfazFormulario):
    
    def __init__(self):
        self.__precio_producto = None
    
    def mostrar(self, data):
        validador_de_numero = data['validador_numero']
        while True:
            try:
                precio_producto = input('\nIngrese precio producto: ')
                numero_validado = validador_de_numero.validar(precio_producto)
                self.__precio_producto = numero_validado
                print(f'-"{validador_de_numero.obtener_datos():,}" valor valido')
                break
            except ValueError as e:
                print(f'\nError: {e}\n--- Por favor, intente de nuevo ---')
        
    def get_obtener_datos(self):
        return self.__precio_producto
    
    

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
    
    

class FormularioSiNo(InterfazFormulario):
    
    def __init__(self):
        self.__Salir_del_programa = None
    
    def mostrar(self, data):
        validar_texto = data['validador_texto']
        while True:
            try:
                salir = input('\nAplicar descuento: (si/no): ')
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
    
    
    
class FormularioDescuento(InterfazFormulario):
    
    def __init__(self):
        self.__descuento = None
    
    def mostrar(self, data):
        validador_limite_descuento = data['validar_limites_descuento']
        validador_de_numero = data['validador_numero']
        while True: 
            try:
                descuento_producto = input('\nIngrese descuento del producto: ')
                validadar_numero = validador_de_numero.validar(descuento_producto)
                validador_limite = validador_limite_descuento.validar(validadar_numero)
                self.__descuento = validador_limite
                print(f'-"{validador_limite_descuento.obtener_datos()}" valor valido')
                break
            except ValueError as e:
                print(f'\nError: {e}\n--- Por favor, intente de nuevo ---')
        
    def get_obtener_datos(self):
        return self.__descuento 