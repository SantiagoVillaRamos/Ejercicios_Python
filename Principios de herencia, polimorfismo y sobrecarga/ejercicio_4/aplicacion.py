"""Define una clase CuentaBancaria con un atributo privado __saldo
y métodos para verificar el saldo antes de realizar depósitos y
retiros. Permite que el saldo solo se consulte y modifique a través
de estos métodos.
."""

from cuenta_bancaria import CuentaBancaria
from ejecutar_accion import ServivioCuentaBancaria
from lista_opciones_usuario import ListaOpcionesAplicacionUsuario
from formulario_opcion_usuario import FormularioOpcionUsuario
from validadores import ValidadorNumero, ValidadorDeTexto, Limites
from logica_opcion_usuario import OpcionesUsuario
from ejecutar_accion import RealizarAccion, RealizarOpcion

class Aplicacion:
    
    """Esta clase es la encarga de dar inicio al programa"""
    
    def main():
        
        # inyeccion de dependencias
        cuenta = CuentaBancaria()
        servicio = ServivioCuentaBancaria(cuenta)
        validadores = { 
            'validador_numero': ValidadorNumero(),
            'validador_texto': ValidadorDeTexto(),
            'validar_limites': Limites()
        }
        
        while True:
            
            lista_opciones_usuario = ListaOpcionesAplicacionUsuario()
            lista_opciones_usuario.lista_opciones_usuario()
            
            # inyeccion de dependencias, formulario opciones usuario
            formulario_opcion_usuario = FormularioOpcionUsuario()
            realizar_opcion = RealizarOpcion(formulario_opcion_usuario)
            realizar_opcion.realizar_opcion(validadores)
            
            # inyeccion de dependencias opciones usuario
            opciones_usuario = OpcionesUsuario()
            ejecutar_accion = RealizarAccion(opciones_usuario)
            
            if ejecutar_accion.realizar_accion_programa(realizar_opcion.mostrar_opcion(), servicio, validadores):
                break


if __name__ == '__main__':
    Aplicacion.main()