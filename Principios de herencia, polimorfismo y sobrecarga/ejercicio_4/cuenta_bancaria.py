from interfaz import InterfazCuentaBancaria



class CuentaBancaria(InterfazCuentaBancaria):
    
    """Clase CuentaBancaria, tiene metodos que manejan
    logica de ingreso de datos, actualizar y mostrar datos 
    """
    
    def __init__(self):
        self.__saldo = [{
            'saldo': 0
        }] 

    
    def set_agregar_saldo(self, datos):
        if self.__saldo[0]['saldo'] == 0:
            self.__saldo[0]['saldo'] = datos
            print(f'\n - Saldo Agregado')
            return True
        else:
            print(f'\n - La cuenta ya tiene saldo')
            return False


    def depositar(self, monto):
        
        if not isinstance(monto, (int, float)) or monto <= 0:
            print("\nError: El monto debe ser un número positivo")
            return False
        
        self.__saldo[0]['saldo'] += monto  
        print(f"\n Depósito exitoso. Saldo actual: ${self.__saldo[0]['saldo']:,}")
        return True



    def retirar(self, monto):
       
        if not isinstance(monto, (int, float)) or monto <= 0:
            print("\n Error: El monto debe ser un número positivo")
            return False
            
        if monto > self.__saldo[0]['saldo']:
            print(f"\n - Error: Fondos insuficientes (Saldo: ${self.__saldo[0]['saldo']:,})")
            return False
            
        self.__saldo[0]['saldo'] -= monto
        print(f"\n Retiro exitoso. (Saldo actual: ${self.__saldo[0]['saldo']:,f})")
        return True


    def get_consultar_saldo(self):
        return self.__saldo[0]['saldo']
