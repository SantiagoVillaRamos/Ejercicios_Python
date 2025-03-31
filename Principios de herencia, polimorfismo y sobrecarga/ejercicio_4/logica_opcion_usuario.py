
from interfaz import InterfazOpciones
from agregar_saldo import AgregarSaldo
from depositar import Depositar
from retirar import Retirar
from consultar_saldo import ConsultarSaldo
from salir import Salir 

class OpcionesUsuario(InterfazOpciones):
    
    # Mapeo de opciones a clases
    def __init__(self):
        self.opciones_de_usuario = {
            1:AgregarSaldo(),
            2:Depositar(),
            3:Retirar(),
            4:ConsultarSaldo(),
            5:Salir() 
        }
     
    def realizar_accion(self, opcion, data, objeto):
        
        opcion_usuario = self.opciones_de_usuario.get(opcion)
        
        if opcion_usuario:
            opcion_usuario.ejecutar(data, objeto)
        else:
            print('\n-Opcion no valida')