from interfaz import InterfazFormulario


class FormularioNombreEmpleado(InterfazFormulario):
    
    def __init__(self):
        self.__nombre_empleado = None
    
    def mostrar(self, data):
        validador_de_texto = data['validador_texto']
        while True:
            try:
                nombre_empleado = input('\nNombre Empleado: ')
                nombre_valido = validador_de_texto.validar(nombre_empleado)
                self.__nombre_empleado = nombre_valido
                print(f'-"{validador_de_texto.obtener_datos()}" valido')
                break
            except ValueError as e:
                print(f'\nError: {e}\n--- Por favor, intente de nuevo ---')
        
    def get_obtener_datos(self):
        return self.__nombre_empleado
 


class FormularioNombreNuevoEmpleado(InterfazFormulario):
    
    def __init__(self):
        self.__nombre_empleado = None
    
    def mostrar(self, data):
        validador_de_texto = data['validador_texto']
        while True:
            try:
                nombre_empleado = input('\nNombre nuevo del Empleado: ')
                nombre_valido = validador_de_texto.validar(nombre_empleado)
                self.__nombre_empleado = nombre_valido
                print(f'-"{validador_de_texto.obtener_datos()}" valido')
                break
            except ValueError as e:
                print(f'\nError: {e}\n--- Por favor, intente de nuevo ---')
        
    def get_obtener_datos(self):
        return self.__nombre_empleado
   
    
      
class FormularioSalarioEmpleado(InterfazFormulario):
    
    def __init__(self):
        self.__salario_empleado = None
    
    def mostrar(self, data):
        validador_de_numero = data['validador_numero']
        while True:
            try:
                salario_empleado = input('\nIngrese salario: ')
                salario_valido = validador_de_numero.validar(salario_empleado)
                self.__salario_empleado = salario_valido
                print(f'-"{validador_de_numero.obtener_datos():,}" valor valido')
                break
            except ValueError as e:
                print(f'\nError: {e}\n--- Por favor, intente de nuevo ---')
        
    def get_obtener_datos(self):
        return self.__salario_empleado
    
    

class FormularioSalirDelPrograma(InterfazFormulario):
    
    def __init__(self):
        self.__Salir_del_programa = None
    
    def mostrar(self, data):
        validar_texto = data['validador_texto']
        while True:
            try:
                salir = input('\n¿Estas seguro de salir ? (si/no): ')
                salir_del_programa = validar_texto.validar(salir)
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
        self.__aplicar_aumento = None
    
    def mostrar(self, data):
        validar_texto = data['validador_texto']
        while True:
            try:
                aplicar_aumento = input('\nAplicar Aumento: (si/no): ')
                aumento_valido = validar_texto.validar(aplicar_aumento)
                print(f'Titulo "{validar_texto.obtener_datos()}" valido')
                self.__aplicar_aumento = aumento_valido
                break
            except ValueError as e:
                print(e)
                print('\t---Por favor, intenta de nuevo.---')
                
    def get_obtener_datos(self):
        return self.__aplicar_aumento
    
    