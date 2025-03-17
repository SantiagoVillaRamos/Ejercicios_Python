class FormularioOpcionUsuario:
    def formulario_opcion_usuario(self):
        while True:
            try:
                opcion_usuario = int(input('\n---Opcion: '))
                if opcion_usuario < 1 or opcion_usuario > 4:
                    raise ValueError('\n\tOpcion invalida')
                break
            except ValueError as e:
                print(e)
                print('\t---Por favor, intenta de nuevo.---')
        
        return opcion_usuario