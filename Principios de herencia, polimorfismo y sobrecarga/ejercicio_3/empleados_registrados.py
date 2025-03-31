from interfaz import InterfazEjecutarAccionUsuario


class EmpleadosRegistrados(InterfazEjecutarAccionUsuario):
    
    def ejecutar(self, data, objeto):
        
        data.lista_empleados()