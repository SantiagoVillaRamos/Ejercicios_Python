from interfaz import InterfazEjecutarAccionUsuario

class Balance(InterfazEjecutarAccionUsuario):
    
    def ejecutar(self, data, objeto):
        
        data.obtener_balance()
    