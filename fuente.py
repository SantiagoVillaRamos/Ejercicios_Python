# clase CadenaTexto que recibe un texto y verifica que no esté vacío ni contenga números. Si la cadena no cumple con estas condiciones, se lanza una excepción ValueError. La clase también tiene un método a_mayusculas que devuelve el texto en mayúsculas. En el programa principal, se solicita al usuario que ingrese una cadena de texto y se crea una instancia de la clase CadenaTexto con el texto ingresado. Si la cadena no cumple con las condiciones, se muestra un mensaje de error y se solicita al usuario que ingrese una nueva cadena. Si la cadena es válida, se muestra el texto ingresado y el texto en mayúsculas. El programa se ejecuta en un bucle hasta que se ingrese una cadena válida.
class CadenaTexto:
    def __init__(self, texto):
        if not texto.strip():
            raise ValueError("La cadena no puede estar vacía o contener solo espacios")
        if any(char.isdigit() for char in texto):
            raise ValueError("La cadena no puede contener números")
        self._texto = texto

    @property
    def texto(self):
        return self._texto

    def a_mayusculas(self):
        return self._texto.upper()
    
    
# clase que recorre la cadena de texto y verifica cuantas letras tiene y cuantas palabras tiene.
class CadenaTexto2:
    def __init__(self, texto):
        self._texto = texto
    
    def contar_letras(self):
        return sum(1 for char in self._texto if char.isalpha())

    def contar_palabras(self):
        return len(self._texto.split())
    

# clase encargada de sumar dos numeros de contar letras y contar palabras
class Suma:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
        
    def suma_de_numeros(self):
        return self.num1 + self.num2


# función principal que solicita al usuario que ingrese una cadena de texto y crea una instancia de la clase CadenaTexto con el texto ingresado. Si la cadena no cumple con las condiciones, se muestra un mensaje de error y se solicita al usuario que ingrese una nueva cadena. Si la cadena es válida, se muestra el texto ingresado y el texto en mayúsculas. El programa se ejecuta en un bucle hasta que se ingrese una cadena válida.
def main():
    while True:
        try:
            entrada = input("Introduce una cadena de texto: ")
            cadena = CadenaTexto(entrada)
            print("Texto ingresado:", cadena.texto)
            print("En mayúsculas:", cadena.a_mayusculas())
            print("Cantidad de letras:", CadenaTexto2(entrada).contar_letras())
            print("Cantidad de palabras:", CadenaTexto2(entrada).contar_palabras())
            suma = Suma(CadenaTexto2(entrada).contar_letras(), CadenaTexto2(entrada).contar_palabras())
            print(f"Suma de {CadenaTexto2(entrada).contar_letras()} y {CadenaTexto2(entrada).contar_palabras()}: {suma.suma_de_numeros()}")
            break
        except ValueError as e:
            print(e)
            print("Por favor, intenta de nuevo.")

if __name__ == "__main__":
    main()