"""Crea una clase Vehiculo con atributos privados
__velocidad_maxima y __marca. Agrega métodos get_marca() y
set_velocidad_maxima() que aseguren la integridad de los datos y
limiten la velocidad máxima a 200
."""

from vehiculo import Vehiculo
from ejecutar_accion import ServivioVehiculo
from lista_opciones_usuario import ListaOpcionesAplicacionUsuario
from formulario_opcion_usuario import FormularioOpcionUsuario
from validadores import ValidadorNumero, ValidadorDeTexto, Limites
from logica_opcion_usuario import OpcionesUsuario
from ejecutar_accion import RealizarAccion, RealizarOpcion

class Aplicacion:
    
    """Esta clase es la encarga de dar inicio al programa"""
    
    def main():
        
        # inyeccion de dependencias
        vehiculo = Vehiculo()
        servicio = ServivioVehiculo(vehiculo)
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