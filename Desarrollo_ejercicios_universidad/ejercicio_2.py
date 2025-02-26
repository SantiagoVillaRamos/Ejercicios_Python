# Crear una clase Rectangulo con atributos largo y ancho. Agregar
# un método que calcule el área. 

# clase que valida que el valor ingrasado sea mayor a 0
class ValidadorDeNumero:
    def __init__(self, numero):
        if numero <= 0:
            raise ValueError(f'\nEl numero {numero} debe ser mayor a 0')
        self.__numero = numero
        
    def get_numero(self):
        return self.__numero

# clase rectangulo que tiene un largo y un ancho y retorna el area
class Rectangulo:
    def __init__(self, largo, ancho):
        self.__largo = largo
        self.__ancho = ancho
        
    def calcular_area(self):
        resultado = self.__largo.get_numero() * self.__ancho.get_numero()
        return resultado

# clase aplicacion que pide un largo y un ancho y valida que sean correctos
class Aplicacion:
    def main():
        while True:
            try:
                numero = int(input('\nIngresa el largo del rectangulo: '))
                largo = ValidadorDeNumero(numero)
                if largo:
                    print(f'Largo Valido: "{largo.get_numero()}"')
                    break
                
            except ValueError as e:
                print(e)
                print('\t---Por favor, intenta de nuevo.---')
        
        while True:
            try:
                numero2 = int(input('\nIngresa el ancho del rectangulo: '))
                ancho = ValidadorDeNumero(numero2)
                if ancho:
                    print(f'Ancho valido: "{ancho.get_numero()}"')
                    break
            except ValueError as e:
                print(e)
                print('\t---Por favor, intenta de nuevo.---')
        
        rectangulo = Rectangulo(largo, ancho)
        print(f'\nEl area del rectangulo es: {rectangulo.calcular_area()}')


# se llama a la clase aplicacion
if __name__ == '__main__':
    Aplicacion.main()