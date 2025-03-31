from interfaz import InterfazPuntos

class Juego(InterfazPuntos):
    
    def __init__(self):
    
        self.__puntuacion = [
            {'puntos': 0}
        ]


    def agregar_puntos(self, puntos):
            
        self.__puntuacion[0]['puntos'] += puntos
        print(f"+{puntos} puntos. Puntuación actual: {self.__puntuacion[0]['puntos']}")
        return True


    def restar_puntos(self, puntos):
            
        if self.__puntuacion[0]['puntos'] - puntos >= 0:
            self.__puntuacion[0]['puntos'] -= puntos
            print(f"-{puntos} puntos. Puntuación actual: {self.__puntuacion[0]['puntos']}")
            return True
        else:
            print(f"Error: No se pueden restar {puntos} puntos (puntuación actual: {self.__puntuacion[0]['puntos']})")
            return False


    def get_consultar_puntuacion(self) -> int:
        
        return self.__puntuacion[0]['puntos']
