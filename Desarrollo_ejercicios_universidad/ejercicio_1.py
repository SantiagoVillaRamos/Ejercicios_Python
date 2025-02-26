# Añadir un método en la clase Persona llamado presentarse, que
#imprima una presentación usando el nombre y edad de la persona


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


# clase persona que tiene un nombre y una edad y retorna un mensaje de presentacion
class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad
    
    def presentarse(self):
        return f'\nHola, soy {self.__nombre} y tengo {self.__edad} años'
    
    
# clase aplicacion que pide un nombre y una edad y valida que sean correctos
class Aplicacion:
    def main():
         
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

        persona = Persona(nombre, edad)
        print(persona.presentarse())
  
  
# se llama a la clase aplicacion      
if __name__ == '__main__':
    Aplicacion.main()