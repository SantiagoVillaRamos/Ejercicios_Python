from interfaz import InterfazVehiculo

class Vehiculo(InterfazVehiculo):
    
    def __init__(self):
        self.__marca_datos = []
    
    
    def agregar_datos(self, datos):
        
        """"Agrega los datos a la lista de diccionarios"""
        
        # valida que el vehiculo no este nuevamente en la lista de diccionarios
        marca = next((marca for marca in self.__marca_datos if marca['nombre'] == datos['nombre']), None)
        if marca:
            print(f"""\n
                  ---------------------------
                  {datos['nombre']} ya existe
                  ---------------------------
            """)
            return False
        
        # valida la velocidad
        if 0 < datos['velocidad'] >= 200:
            print(f"""\n
                  ---------------------------
                  La velocidad "{datos['velocidad']} km/ph" debe ser menor a 200
                  ---------------------------
            """)
            return False
        
        # guarda los datos
        self.__marca_datos.append(datos)
        print(f"""\n
              ---------------------------
              Se agrego {datos['nombre']}
              ---------------------------
        """)
        return True
    
    
    def set_velocidad_maxima(self, nombre, nueva_velocidad):
        
        marca_vehiculo = next((marca for marca in self.__marca_datos if marca['nombre'] == nombre), None)
        if not marca_vehiculo:
            print(f'\n - "{nombre}" no existe en la base de datos -')
            return False
        
        
        velocidad_anterior = marca_vehiculo['velocidad']
        if 0 < nueva_velocidad <= 200:
            marca_vehiculo['velocidad'] = nueva_velocidad
            print(f"""
                  -------------------------------
                  ------------ Resumen ----------
                  Vehiculo: {nombre}             
                  Vel. Ant:  {velocidad_anterior} km/ph 
                  Vel. Nueva:   {nueva_velocidad} km/ph
                  -------------------------------
            """)
            return True
        else:
            print(f"Error: La velocidad debe estar entre 0-200 km/ph (se recibió {nueva_velocidad})")
            return False
    
    
    # Métodos para marca (solo getter)
    def get_marca(self):
        """Devuelve la marca del vehículo"""
        return self.__marca_datos

