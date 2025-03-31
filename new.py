# clase que maneja las excepciones de la cadena de texto
class CadenaTexto:
    def __init__(self, texto):
        if not texto.strip():
            raise ValueError("\t---La cadena no puede estar vacía o contener solo espacios---")
        if any(char.isdigit() for char in texto):
            raise ValueError("\t---La cadena no puede contener números---")
        self._texto = texto
    
    @property
    def texto(self):
        return self._texto

# funcion que maneja las excepciones de la cadena de texto, verifica que solo sea una letra
def es_una_letra(texto):
    return len(texto) == 1 and texto.isalpha()

# funcion main que solicita al usuario que ingrese un texto y lo agrega a una lista. Si el texto está vacío o contiene números, se lanza una excepción ValueError. El programa se ejecuta en un bucle hasta que se ingrese un texto válido.
def main():
    new_list = []
    text = ""
    while text != "n":
        while True:
            try:
                text = input("\n---Ingresa 's' para ingresar un texto o 'n' para salir: ")
                if es_una_letra(text):
                    print(f"\t---Has introducido la letra '{text}'---")
                    break
                else:
                    raise ValueError("\t---Por favor, introduce solo una letra---")
            except ValueError as e:
                print(e)
                print("\t---Por favor, intenta de nuevo.---")   
                
        if text == "s":
            while True:
                try:
                    text_input = input("\n---Ingresa un texto: ")
                    cadena = CadenaTexto(text_input)
                    new_list.append(cadena.texto)
                    break
                except ValueError as e:
                    print(e)
                    print("\t---Por favor, intenta de nuevo.---")
        elif text == "n":
            print("Gracias por participar.")
            print("\n---Texto ingresado:", new_list)

if __name__ == "__main__":
  main()
