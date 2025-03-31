
from interfaz import InterfazOpciones
from agregar_datos_persona import AgregarDatosPersona
from nombre_nuevo import NuevoNombreEmpleado
from aumentar_salario import AumentoSalario
from nuevo_salario import AumentarSalarioEmpleado
from empleados_registrados import EmpleadosRegistrados
from salir import Salir 

class OpcionesUsuario(InterfazOpciones):
    
    # Mapeo de opciones a clases
    def __init__(self):
        self.opciones_de_usuario = {
            1:AgregarDatosPersona(),
            2:NuevoNombreEmpleado(),
            3:AumentoSalario(),
            4:AumentarSalarioEmpleado(),
            5:EmpleadosRegistrados(),
            6:Salir(),
        }
     
    def realizar_accion(self, opcion, data, objeto):
        
        opcion_usuario = self.opciones_de_usuario.get(opcion)
        
        if opcion_usuario:
            opcion_usuario.ejecutar(data, objeto)
        else:
            print('\n-Opcion no valida')