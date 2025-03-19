class ListaOpcionesAplicacion:
    def lista_opciones_aplicacion(self):
        lista_opciones = ['Agregar cancion', 'Eliminar cancion', 'Actualizar cancion', 'Salir']
        print('\nSelecciona una opcion:')
        
        # recorre las opciones y las muestra por pantanlla
        for i, opcion in enumerate(lista_opciones):
            print(f'{i+1}. {opcion}')  