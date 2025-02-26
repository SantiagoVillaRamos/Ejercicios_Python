# Crear una clase Calculadora con métodos sumar, restar,
# multiplicar, y un método estático convertir_a_entero que convierta
# números de coma flotante a enteros.

# clase calculadora que tiene metodos para sumar, restar y multiplicar
class Calculadora:
    def sumar(self, numero1, numero2):
        return numero1 + numero2
    
    def restar(self, numero1, numero2):
        return numero1 - numero2
    
    def multiplicar(self, numero1, numero2):
        return numero1 * numero2
    
    # metodo estatico que convierte un numero de coma flotante a entero
    @staticmethod
    def convertir_a_entero(numero):
        return int(numero)
    
# clase aplicacion que pide dos numeros y realiza las operaciones de suma, resta y multiplicacion
class Aplicacion:
    def main():
        # se crea una lista de opciones
        opciones = ['Sumar', 'Restar', 'Multiplicar']
        print('\nSelecciona una opcion:')
        # se imprime la lista de opciones
        for i, opcion1 in enumerate(opciones):
            print(f'{i+1}. {opcion1}')
            
        while True:
            try:
                opcion = int(input('\n---Opcion: '))
                if opcion < 1 or opcion > 3:
                    raise ValueError('\n\tOpcion invalida')
                break
            except ValueError as e:
                print(e)
                print('\t---Por favor, intenta de nuevo.---')
        
        while True:
            try:
                numero1 = float(input('\nIngresa el primer numero: '))
                numero_convertido1 = Calculadora.convertir_a_entero(numero1)
                break
            except ValueError as e:
                print(e)
                print('\t---Por favor, intenta de nuevo.---')
                
        while True:
            try:
                numero2 = float(input('\nIngresa el segundo numero: '))
                numero_convertido2 = Calculadora.convertir_a_entero(numero2)
                break
            except ValueError as e:
                print(e)
                print('\t---Por favor, intenta de nuevo.---')
                
        calculadora = Calculadora()
        if opcion == 1:
            print(f'\nResultado de la suma: {calculadora.sumar(numero_convertido1, numero_convertido2)}')
        elif opcion == 2:
            print(f'\nResultado de la resta: {calculadora.restar(numero_convertido1, numero_convertido2)}')
        elif opcion == 3:
            print(f'\nResultado de la multiplicacion: {calculadora.multiplicar(numero_convertido1, numero_convertido2)}')
            
# se llama a la clase aplicacion
if __name__ == '__main__':
    Aplicacion.main()