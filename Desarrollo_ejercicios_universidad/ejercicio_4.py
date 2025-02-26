# Implementa una clase Persona con los atributos nombre, edad, y
# ciudad. Incluye un método saludar que imprima un saludo como:
# “Hola, me llamo [nombre], tengo [edad] años y vivo en [ciudad]”.
# Crea dos o tres instancias de Persona y llama al método saludar
# para cada una.

# clase que valida que la cadena no este vacia y no tenga numeros
class ValidadorDeTexto:
    def __init__(self, texto):
        if not texto.strip():
            raise ValueError(f'\t---La cadena de texto no puede estar vacío')
        if any(char.isdigit() for char in texto):
            raise ValueError(f'\t---El nombre "{texto}" no puede contener números')
        self.__texto = texto
        
    def get_nombre(self):
        return self.__texto

# clase que valida que el numero sea mayor a 0
class ValidadorDeNumero:
    def __init__(self, numero):
        if numero <= 0:
            raise ValueError(f'\nLa Edad {numero} debe ser mayor a 0')
        elif numero >= 120:
            raise ValueError(f'\tLa Edad {numero} debe ser menor a 120')
        self.__numero = numero
        
    def get_numero(self):
        return self.__numero
    
# clase persona que tiene un nombre, una edad y una ciudad y retorna un mensaje de presentacion
class Persona:
    def __init__(self, nombre, edad, ciudad):
        self.__nombre = nombre
        self.__edad = edad
        self.__ciudad = ciudad
    
    def saludar(self):
        return f'\tHola, me llamo {self.__nombre}, tengo {self.__edad} años y vivo en {self.__ciudad}'
    
# clase aplicacion que pide un nombre, una edad y una ciudad y valida que sean correctos
class Aplicacion:
    def main():
        # se crea una lista de personas vacia
        personas = []
        # se pide el nombre, la edad y la ciudad de la persona
        for i in range(3):
            while True:
                try:
                    nombre = input('\nIngresa tu nombre:')
                    objecto_nombre = ValidadorDeTexto(nombre)    
                    if objecto_nombre:
                        print(f'Nombre "{objecto_nombre.get_nombre()}" valido')
                        break
            
                except ValueError as e:
                    print(e)
                    print('\t---Por favor, intenta de nuevo.---')
                    
            while True:
                try:
                    edad = int(input('\nIngresa tu edad:'))
                    if ValidadorDeNumero(edad):
                        print('Edad valida')
                        break
                except ValueError as e:
                    print(e)
                    print('\t---Por favor, intenta de nuevo.---')
            
            while True:
                try:
                    ciudad = input('\nIngresa tu ciudad:')
                    objecto_ciudad = ValidadorDeTexto(ciudad)    
                    if objecto_ciudad:
                        print(f'Ciudad "{objecto_ciudad.get_nombre()}" valida')
                        break
                except ValueError as e:
                    print(e)
                    print('\t---Por favor, intenta de nuevo.---')
            # se crea un objeto persona y se agrega a la lista de personas
            persona = Persona(objecto_nombre.get_nombre(), edad, objecto_ciudad.get_nombre())
            personas.append(persona)
            
        # se recorre la lista de personas y se llama al metodo saludar
        for persona in personas:
            print(persona.saludar())
            
# se llama a la clase aplicacion            
if __name__ == '__main__':
    Aplicacion.main()