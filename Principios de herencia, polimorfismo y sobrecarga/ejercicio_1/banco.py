from interfaz import InterfazBanco


class Banco(InterfazBanco):
    
    def __init__(self):
        self._balance = 0

    def depositar(self, cantidad):
        
        if cantidad <= 0:
            print("Error: La cantidad a depositar debe ser positiva.")
            return False
        
        if cantidad > 0:
            self._balance += cantidad
            print(f"Depósito exitoso")
            return True
            

    def retirar(self, cantidad):
        
        if cantidad <= 0:
            print(f"\n La Cantidad a retirar debe ser positiva")
            return False
            
        if cantidad > self._balance:
            print(f"Error: Fondos insuficientes. Balance ( $ {self._balance:,})")
            return False
        
        self._balance -= cantidad
        print(f"""
              --- Resumen ---
              Retiro: $ {cantidad:,}
              Balance: $ {self._balance:,}
        """)


    def obtener_balance(self):
        return self._balance
    