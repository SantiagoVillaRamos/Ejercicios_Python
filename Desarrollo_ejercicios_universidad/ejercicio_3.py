# Crear una clase abstracta Empleado con un método
# calcular_salario. Luego crear Gerente y Vendedor, cada uno con su
# propia fórmula para calcular el salario. 

from abc import ABC, abstractmethod
# clase abstracta empleado con un metodo calcular salario
class Empleado(ABC):
    @abstractmethod
    def calcular_salario(self):
        pass

# clase gerente que hereda de empleado y tiene un salario base y una comision
class Gerente(Empleado):
    def __init__(self, salario_base, comision):
        self.__salario_base = salario_base
        self.__comision = comision
    
    def calcular_salario(self):
        return self.__salario_base + self.__comision

# clase vendedor que hereda de empleado y tiene un salario base y una comision   
class Vendedor(Empleado):
    def __init__(self, salario_base, comision):
        self.__salario_base = salario_base
        self.__comision = comision
    
    def calcular_salario(self):
        return self.__salario_base + self.__comision

# clase aplicacion que pide un tipo de empleado, un salario base y una comision y valida que sean correctos  
class Aplicacion:
    personas = ['Gerente', 'Vendedor']
    def main():
        print('Selecciona el tipo de empleado:')
        for i, persona in enumerate(Aplicacion.personas):
            print(f'{i+1}. {persona}')
        
        while True:
            try:
                opcion = int(input('\n---Opcion: '))
                if opcion < 1 or opcion > 2:
                    raise ValueError('\n\tOpcion invalida')
                break
            except ValueError as e:
                print(e)
                print('\t---Por favor, intenta de nuevo.---')
                
        while True:
            try:
                salario_base = int(input('\nIngresa el salario base: '))
                if salario_base <= 0:
                    raise ValueError('\n\tEl salario base debe ser mayor a 0')
                break
            except ValueError as e:
                print(e)
                print('\t---Por favor, intenta de nuevo.---')
                
        while True:
            try:
                comision = int(input('\nIngresa la comision: '))
                if comision <= 0:
                    raise ValueError('\n\tLa comision debe ser mayor a 0')
                break
            except ValueError as e:
                print(e)
                print('\t---Por favor, intenta de nuevo.---')
                
        # se crea un objeto de la clase gerente o vendedor dependiendo de la opcion
        if opcion == 1:
            gerente = Gerente(salario_base, comision)
            print(f'\nEl salario del gerente es: {gerente.calcular_salario()}')
        else:
            vendedor = Vendedor(salario_base, comision)
            print(f'\nEl salario del vendedor es: {vendedor.calcular_salario()}')
        
# se llama a la clase aplicacion        
if __name__ == '__main__':
    Aplicacion.main()