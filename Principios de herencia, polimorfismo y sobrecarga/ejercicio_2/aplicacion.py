"""Crea una clase Producto con un atributo __precio y métodos
set_precio() y get_precio() para modificar y obtener el precio de
forma segura. Añade un método aplicar_descuento(porcentaje)
que modifique el precio usando encapsulamiento."""

from producto import Producto
from ejecutar_accion import ServicioVentas
from lista_opciones_usuario import ListaOpcionesAplicacionUsuario
from formulario_opcion_usuario import FormularioOpcionUsuario
from validadores import ValidadorNumero, ValidadorDeTexto, Limites, LimitesDescuentos
from logica_opcion_usuario import OpcionesUsuario
from ejecutar_accion import RealizarAccion, RealizarOpcion

class Aplicacion:
    
    def main():
        
        # inyeccion de dependencias
        producto = Producto()
        servicio = ServicioVentas(producto)
        validadores = {
            'validador_numero': ValidadorNumero(),
            'validador_texto': ValidadorDeTexto(),
            'validar_limites': Limites(),
            'validar_limites_descuento': LimitesDescuentos()
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

            
            if ejecutar_accion.realizar_accion_programa(realizar_opcion.mostrar_opcion(), servicio, validadores):
                break


if __name__ == '__main__':
    Aplicacion.main()