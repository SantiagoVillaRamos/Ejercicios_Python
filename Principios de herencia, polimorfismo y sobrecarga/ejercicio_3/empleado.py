from interfaz import InterfazEmpleado

class Empleado(InterfazEmpleado):
    
    """
    Es donde esta la lista de diccionarios. Utiliza metodos
    para agregar datos; como el metodo agregar_datos_persona(datos), los 
    agrega a la lista de diccionarios. Metodos como set_nombre_nuevo() y 
    set_nuevo_salario(); encargados de actualizar datos.
    """
    
    def __init__(self): 
        self.__datos_persona = []
        
        
    def agregar_datos_persona(self, datos):
        """guardar datos del empleado"""
        if any(persona['nombre'] == datos['nombre'] for persona in self.__datos_persona):
            print(f"\nError: '{datos['nombre']}' ya existe")
            return False  
            
        self.__datos_persona.append(datos)
        print(f"\nRegistro exitoso: {datos['nombre']}")
        return True
    
    
    def set_nombre_nuevo(self, nombre_persona, nuevo_nombre):
        
        """Cambiar el nombre del empleado"""
        # verificar si el usuario existe
        empleado = next((persona for persona in self.__datos_persona if persona['nombre'] == nombre_persona), None)
        if not empleado:
            print(f"\n --- El nombre {nombre_persona} no existe en la base de datos ---")
            return False
        
        # cambiar nombre
        nombre_original = empleado['nombre']
        empleado['nombre'] = nuevo_nombre
        
        print(f"""
            --- Resumen ---
            Nombre anterior: {nombre_original}
            Nombre nuevo: {nuevo_nombre}
            Salario: {empleado['salario']:,}
        """)
        print(f"""
            --- Se actualiza el nombre {nombre_persona} a {nuevo_nombre} ---  
        """)
        return True                
            
            
            
    def aumentar_salario(self, nombre_persona, aumento):
        """Aumenta el salario solo si el aumento es positivo"""
        
        # validacion 1: ¿existe el empleado?
        empleado = next((persona for persona in self.__datos_persona if persona['nombre'] == nombre_persona), None)
        if not empleado:
            print(f"\n --- El nombre {nombre_persona} no existe en la base de datos ---")
            return False
        
        # Validacion 2: aumento positivo
        if aumento <= 0:
            print('\n --- Error: El aumento debe ser un numero positivo ---')
            return False
        
        # procesar aumento
        salario_anterior = empleado['salario']
        empleado['salario'] += aumento
        
        print(f"""
            --- Resumen ---
            Persona: {nombre_persona}
            Salario anterior: {salario_anterior:,}
            Nuevo salario: {empleado['salario']:,}
            Ingremento de: {aumento:,}
        """)
        print(f'\n-Se aumento el Salario de {nombre_persona}')
        return True
        
    
    
    def set_nuevo_salario(self, nombre_persona, nuevo_salario):
        """Solo permite establecer un salario mayor al actual"""
        
        # validacion 1: ¿existe el empleado?
        empleado = next((persona for persona in self.__datos_persona if persona['nombre'] == nombre_persona), None)
        if not empleado:
            print(f"\n --- El nombre {nombre_persona} no existe en la base de datos ---")
            return False
        
        # validacion 2: si el salario es menor al actual
        persona_salario_anterior = empleado['salario']
        if nuevo_salario <= persona_salario_anterior:
            print(f"\nError: El nuevo salario ({nuevo_salario}) debe ser mayor al actual ({persona_salario_anterior})")
            return False
        
        # actualizar salario
        empleado['salario'] = nuevo_salario
        print(f"""\n
        --- Resumen ---
        Empleado: {nombre_persona}
        Salario anterior: {persona_salario_anterior:,}
        Nuevo salario: {nuevo_salario:,}
        """)
        return True
        
            
    def get_lista_empleados(self):
        return self.__datos_persona
    
    def get_nombre(self):
        return self.__datos_persona[-1]['nombre']
    