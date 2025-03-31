
"""Crea una clase Banco con un atributo privado _balance. Agrega
métodos depositar() y retirar() que verifiquen el acceso al balance
de forma controlada"""


from validadores import ValidadorNumero, ValidadorDeTexto, Limites
from banco import Banco
from lista_opciones_usuario import ListaOpcionesAplicacionUsuario
from formulario_opcion_usuario import FormularioOpcionUsuario
from logica_opcion_usuario import OpcionesUsuario
from ejecutar_accion import RealizarAccion, BancoNegocio, RealizarOpcion
 
# clase aplicacion 
class Aplicacion: 
    
    def main():
        
        # inyeccion de dependencias
        banco = Banco()
        banco_negocio = BancoNegocio(banco)
        validadores = {
            'validador_numero': ValidadorNumero(),
            'validador_texto': ValidadorDeTexto(),
            'validar_limites': Limites(),
        }
        
        while True:
            
            lista_opciones_usuario = ListaOpcionesAplicacionUsuario()
            lista_opciones_usuario.lista_opciones_usuario()

            formulario_opcion_usuario = FormularioOpcionUsuario()
            realizar_opcion = RealizarOpcion(formulario_opcion_usuario)
            realizar_opcion.realizar_opcion(validadores)
            
            # inyeccion de dependencias
            opciones_usuario = OpcionesUsuario()
            ejecutar_accion = RealizarAccion(opciones_usuario)
            
            if ejecutar_accion.realizar_accion_programa(realizar_opcion.mostrar_opcion(), banco_negocio, validadores):
                break


if __name__ == '__main__':
    Aplicacion.main()