
class ListaOpcionesAplicacionUsuario:
    # metodo que muestra las opciones de la aplicacion
    def lista_opciones_usuario(self):
        lista_opciones = ['Ingresar nombre y salario del empleado', 'Cambiar el nombre del empleado', 'Aumentar salario del empleado', 'Nuevo Salario del empleado', 'Listar Empleados Registrados', 'Salir']
        print('\nSelecciona una opcion:')
        
        # recorre las opciones y las muestra por pantanlla
        for i, opcion in enumerate(lista_opciones):
            print(f'{i+1}. {opcion}') 