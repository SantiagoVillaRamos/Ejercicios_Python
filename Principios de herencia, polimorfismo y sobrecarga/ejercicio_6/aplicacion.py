"""Define una clase Juego con un atributo privado __puntuacion.
Agrega métodos para añadir y restar puntos solo si el valor total
no es negativo. Asegura que la puntuación solo pueda ser
accedida y modificada a través de métodos específicos."""

from juego import Juego
from ejecutar_accion import ServivioPuntuacion
from lista_opciones_usuario import ListaOpcionesAplicacionUsuario
from formulario_opcion_usuario import FormularioOpcionUsuario
from validadores import ValidadorNumero, ValidadorDeTexto, Limites
from logica_opcion_usuario import OpcionesUsuario
from ejecutar_accion import RealizarAccion, RealizarOpcion

class Aplicacion:
    
    """Esta clase es la encarga de dar inicio al programa"""
    
    def main():
        
        # inyeccion de dependencias
        juego = Juego()
        servicio = ServivioPuntuacion(juego)
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