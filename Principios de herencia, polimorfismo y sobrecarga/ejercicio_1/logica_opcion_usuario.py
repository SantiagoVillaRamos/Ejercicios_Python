
from interfaz import InterfazOpciones
from depositar_dinero import DepositarDinero
from retirar_dinero import RetirarDinero
from balance import Balance
from salir import Salir

class OpcionesUsuario(InterfazOpciones):
    
    # Mapeo de opciones a clases
    def __init__(self):
        self.opciones_de_usuario = {
            1:DepositarDinero(),
            2:RetirarDinero(),
            3:Balance(),
            4:Salir(), 
        }
    
    def realizar_accion(self, opcion, data, objeto):
        
        opcion_usuario = self.opciones_de_usuario.get(opcion)
        
        if opcion_usuario:
            opcion_usuario.ejecutar(data, objeto)
        else:
            print('\n-Opcion no valida')