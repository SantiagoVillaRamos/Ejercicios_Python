
class ListaOpcionesAplicacionUsuario:
    # metodo que muestra las opciones de la aplicacion
    def lista_opciones_usuario(self):
        lista_opciones = ['Ingresar Producto y Precio', 'Actualizar Precio', 'Agregar Descuento a Producto', 'listar productos', 'Salir']
        print('\nSelecciona una opcion:')
        
        # recorre las opciones y las muestra por pantanlla
        for i, opcion in enumerate(lista_opciones):
            print(f'{i+1}. {opcion}') 